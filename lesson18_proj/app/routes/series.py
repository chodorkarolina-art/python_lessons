# lesson18_task5

"""
Obsługa cyklicznych rezerwacji.

Funkcjonalności:
1. Tworzenie serii rezerwacji WEEKLY lub BIWEEKLY.
2. Wspólny identyfikator series_id.
3. Sprawdzanie konfliktów wszystkich terminów.
4. Anulowanie jednej rezerwacji.
5. Anulowanie całej serii.
"""

import uuid
from datetime import datetime

from dateutil.rrule import WEEKLY, rrule
from flask import Blueprint, jsonify, request

from app.db import db
from app.models.booking import Booking
from app.models.room import Room
from app.models.user import User


# lesson18_task5 - blueprint rezerwacji cyklicznych
series_bp = Blueprint(
    "series",
    __name__,
    url_prefix="/api/series"
)


# =========================================================
# lesson18_task5
# TWORZENIE SERII REZERWACJI
# POST /api/series/
# =========================================================

@series_bp.route("/", methods=["POST"])
def create_series():
    """
    Tworzy serię rezerwacji cyklicznych.

    Obsługiwane reguły:
    - WEEKLY: co tydzień,
    - BIWEEKLY: co dwa tygodnie.
    """

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Brak danych JSON"
        }), 400

    required_fields = [
        "room_id",
        "user_id",
        "title",
        "start_time",
        "end_time",
        "recurrence_rule",
        "weeks"
    ]

    missing_fields = [
        field
        for field in required_fields
        if field not in data
    ]

    if missing_fields:
        return jsonify({
            "error": "Brak wymaganych pól",
            "missing_fields": missing_fields
        }), 400

    # lesson18_task5 - konwersja dat
    try:
        start_time = datetime.fromisoformat(
            data["start_time"]
        )

        end_time = datetime.fromisoformat(
            data["end_time"]
        )

        occurrences_count = int(
            data["weeks"]
        )

    except (ValueError, TypeError):
        return jsonify({
            "error": (
                "Niepoprawny format daty lub liczby powtórzeń. "
                "Daty podaj w formacie ISO."
            )
        }), 400

    if start_time >= end_time:
        return jsonify({
            "error": (
                "Czas rozpoczęcia musi być wcześniejszy "
                "niż czas zakończenia"
            )
        }), 400

    if occurrences_count < 1:
        return jsonify({
            "error": "Liczba powtórzeń musi być większa od zera"
        }), 400

    # lesson18_task5 - sprawdzenie sali
    room = db.session.get(
        Room,
        data["room_id"]
    )

    if room is None:
        return jsonify({
            "error": "Sala nie istnieje"
        }), 404

    if not room.is_active:
        return jsonify({
            "error": "Sala jest nieaktywna"
        }), 400

    # lesson18_task5 - sprawdzenie użytkownika
    user = db.session.get(
        User,
        data["user_id"]
    )

    if user is None:
        return jsonify({
            "error": "Użytkownik nie istnieje"
        }), 404

    recurrence = str(
        data["recurrence_rule"]
    ).upper()

    if recurrence == "WEEKLY":
        interval = 1

    elif recurrence == "BIWEEKLY":
        interval = 2

    else:
        return jsonify({
            "error": (
                "Niepoprawna reguła. "
                "Dozwolone wartości: WEEKLY, BIWEEKLY"
            )
        }), 400

    booking_duration = end_time - start_time

    # lesson18_task5 - generowanie terminów
    occurrence_dates = list(
        rrule(
            freq=WEEKLY,
            interval=interval,
            count=occurrences_count,
            dtstart=start_time
        )
    )

    conflicts = []

    # lesson18_task5
    # Sprawdzamy wszystkie terminy przed zapisaniem serii.
    for occurrence_start in occurrence_dates:
        occurrence_end = (
            occurrence_start + booking_duration
        )

        conflict = Booking.query.filter(
            Booking.room_id == room.id,
            Booking.status != "cancelled",

            # Rezerwacje nachodzą na siebie, gdy:
            Booking.start_time < occurrence_end,
            Booking.end_time > occurrence_start
        ).first()

        if conflict:
            conflicts.append({
                "requested_start": (
                    occurrence_start.isoformat()
                ),
                "requested_end": (
                    occurrence_end.isoformat()
                ),
                "conflicting_booking_id": conflict.id,
                "conflicting_title": conflict.title,
                "conflicting_start": (
                    conflict.start_time.isoformat()
                ),
                "conflicting_end": (
                    conflict.end_time.isoformat()
                )
            })

    # Jeśli choć jeden termin jest zajęty,
    # nie tworzymy żadnej rezerwacji z serii.
    if conflicts:
        return jsonify({
            "error": (
                "Nie można utworzyć serii. "
                "Niektóre terminy są zajęte."
            ),
            "conflicts": conflicts
        }), 409

    # lesson18_task5 - wspólny UUID całej serii
    series_id = str(
        uuid.uuid4()
    )

    created_bookings = []

    try:
        # lesson18_task5 - tworzenie wszystkich rezerwacji
        for occurrence_start in occurrence_dates:
            occurrence_end = (
                occurrence_start + booking_duration
            )

            booking = Booking(
                room_id=room.id,
                user_id=user.id,
                title=data["title"],
                description=data.get("description"),
                start_time=occurrence_start,
                end_time=occurrence_end,
                status="confirmed",
                attendees_count=data.get(
                    "attendees_count",
                    1
                ),
                recurrence_rule=recurrence,
                series_id=series_id
            )

            db.session.add(booking)

            created_bookings.append(booking)

        db.session.commit()

    except Exception as error:
        db.session.rollback()

        return jsonify({
            "error": "Nie udało się utworzyć serii",
            "details": str(error)
        }), 500

    return jsonify({
        "message": "Seria utworzona",
        "series_id": series_id,
        "recurrence_rule": recurrence,
        "count": len(created_bookings),
        "bookings": [
            {
                "id": booking.id,
                "start_time": (
                    booking.start_time.isoformat()
                ),
                "end_time": (
                    booking.end_time.isoformat()
                ),
                "status": booking.status
            }
            for booking in created_bookings
        ]
    }), 201


# =========================================================
# lesson18_task5
# ANULOWANIE POJEDYNCZEJ REZERWACJI
# POST /api/series/booking/<booking_id>/cancel
# =========================================================

@series_bp.route(
    "/booking/<int:booking_id>/cancel",
    methods=["POST"]
)
def cancel_booking(booking_id):
    """
    Anuluje jedną wybraną rezerwację.
    Pozostałe rezerwacje z serii pozostają aktywne.
    """

    booking = db.session.get(
        Booking,
        booking_id
    )

    if booking is None:
        return jsonify({
            "error": "Rezerwacja nie istnieje"
        }), 404

    if booking.status == "cancelled":
        return jsonify({
            "message": "Rezerwacja była już anulowana",
            "booking_id": booking.id
        }), 200

    booking.status = "cancelled"

    db.session.commit()

    return jsonify({
        "message": "Rezerwacja anulowana",
        "booking_id": booking.id,
        "series_id": booking.series_id,
        "status": booking.status
    })


# =========================================================
# lesson18_task5
# ANULOWANIE CAŁEJ SERII
# POST /api/series/<series_id>/cancel
# =========================================================

@series_bp.route(
    "/<string:series_id>/cancel",
    methods=["POST"]
)
def cancel_series(series_id):
    """
    Anuluje wszystkie aktywne rezerwacje
    należące do podanej serii.
    """

    bookings = Booking.query.filter_by(
        series_id=series_id
    ).all()

    if not bookings:
        return jsonify({
            "error": "Seria o podanym ID nie istnieje"
        }), 404

    cancelled_count = 0

    for booking in bookings:
        if booking.status != "cancelled":
            booking.status = "cancelled"
            cancelled_count += 1

    db.session.commit()

    return jsonify({
        "message": "Seria anulowana",
        "series_id": series_id,
        "series_bookings_count": len(bookings),
        "cancelled_count": cancelled_count
    })