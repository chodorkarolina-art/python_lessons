# lesson18_task4

"""
Endpointy systemu powiadomień.

Zadanie obejmuje:
1. Pobieranie nieprzeczytanych powiadomień.
2. Oznaczanie powiadomienia jako przeczytane.
3. Tworzenie przypomnień przed rezerwacją.
"""

from datetime import datetime, timedelta

from flask import Blueprint, jsonify

from app.db import db
from app.models.booking import Booking
from app.models.notification import Notification


# lesson18_task4 - blueprint powiadomień
notifications_bp = Blueprint(
    "notifications",
    __name__,
    url_prefix="/api/notifications"
)


# lesson18_task4
# LISTA NIEPRZECZYTANYCH POWIADOMIEŃ
# GET /api/notifications/


@notifications_bp.route("/", methods=["GET"])
def get_notifications():
    """
    Zwraca tylko nieprzeczytane powiadomienia,
    posortowane od najnowszego.
    """

    notifications = (
        Notification.query
        .filter_by(is_read=False)
        .order_by(Notification.created_at.desc())
        .all()
    )

    return jsonify([
        {
            "id": notification.id,
            "user_id": notification.user_id,
            "message": notification.message,
            "is_read": notification.is_read,
            "created_at": notification.created_at.isoformat()
        }
        for notification in notifications
    ])



# lesson18_task4
# OZNACZENIE POWIADOMIENIA JAKO PRZECZYTANE
# POST /api/notifications/<id>/read


@notifications_bp.route(
    "/<int:notification_id>/read",
    methods=["POST"]
)
def mark_as_read(notification_id):
    """
    Ustawia is_read=True dla wybranego powiadomienia.
    """

    notification = Notification.query.get_or_404(
        notification_id
    )

    notification.is_read = True

    db.session.commit()

    return jsonify({
        "message": "Powiadomienie oznaczone jako przeczytane",
        "notification_id": notification.id,
        "is_read": notification.is_read
    })


# lesson18_task4
# PRZYPOMNIENIA PRZED REZERWACJĄ
# GET /api/notifications/check-reminders


@notifications_bp.route(
    "/check-reminders",
    methods=["GET"]
)
def check_reminders():
    """
    Wyszukuje potwierdzone rezerwacje rozpoczynające się
    w przedziale od jednej do dwóch godzin od teraz.

    Dla każdej rezerwacji tworzy powiadomienie,
    jeśli identyczne przypomnienie jeszcze nie istnieje.
    """

    now = datetime.now()

    in_one_hour_start = now + timedelta(hours=1)
    in_one_hour_end = now + timedelta(hours=2)

    bookings = (
        Booking.query
        .filter(
            Booking.start_time >= in_one_hour_start,
            Booking.start_time <= in_one_hour_end,
            Booking.status == "confirmed"
        )
        .all()
    )

    created_count = 0

    for booking in bookings:
        reminder_message = (
            f"Przypomnienie: rezerwacja "
            f"'{booking.title}' zaczyna się za godzinę"
        )

        # lesson18_task4
        # Zapobieganie tworzeniu kilku takich samych przypomnień
        existing_notification = (
            Notification.query
            .filter_by(
                user_id=booking.user_id,
                message=reminder_message
            )
            .first()
        )

        if existing_notification:
            continue

        notification = Notification(
            user_id=booking.user_id,
            message=reminder_message,
            is_read=False,
            created_at=datetime.now()
        )

        db.session.add(notification)

        created_count += 1

    db.session.commit()

    return jsonify({
        "message": f"Utworzono {created_count} przypomnień"
    })