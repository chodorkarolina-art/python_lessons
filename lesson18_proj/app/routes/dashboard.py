"""
Dashboard aplikacji, test połączenia z bazą
oraz demonstracja problemu N+1.
"""

from time import time

from flask import Blueprint, jsonify, render_template
from sqlalchemy import event, text
from sqlalchemy.orm import joinedload

from app.db import db
from app.models import Booking
from app.services import dashboard_service as ds


dashboard_bp = Blueprint(
    "dashboard",
    __name__
)

# DASHBOARD

@dashboard_bp.route("/dashboard")
def dashboard():
    """
    Wyświetla główny dashboard aplikacji.
    """

    # Podstawowe dane dashboardu
    stats, upcoming, top_users, room_utilization = (
        ds.get_dashboard_summary()
    )

    # lesson18_task3
    # Dane do wykresów i dodatkowych statystyk
    dashboard_api_data = ds.get_dashboard_api_stats()

    return render_template(
        "dashboard.html",
        stats=stats,
        upcoming=upcoming,
        top_users=top_users,
        room_utilization=room_utilization,

        # lesson18_task3
        department_stats=dashboard_api_data.get(
            "department_stats",
            []
        )
    )


# LESSON18_TASK3 – API ZE STATYSTYKAMI

# lesson18_task3
@dashboard_bp.route("/api/dashboard/stats")
def dashboard_api_stats():
    """
    Zwraca dane statystyczne w formacie JSON.

    Dane mogą zawierać:
    - statystyki podstawowe,
    - rezerwacje według departamentów,
    - heatmapę,
    - trend z ostatnich 30 dni.
    """

    return jsonify(
        ds.get_dashboard_api_stats()
    )

# LESSON18_TASK1 – TEST POŁĄCZENIA Z BAZĄ

# lesson18_task1
@dashboard_bp.route("/test-db")
def test_db():
    """
    Sprawdza prawdziwe połączenie z bazą danych.

    Zapytanie SELECT 1 jest wykonywane bezpośrednio
    w aktualnie skonfigurowanej bazie.
    """

    try:
        db.session.execute(
            text("SELECT 1")
        )

        database_address = db.engine.url.render_as_string(
            hide_password=True
        )

        return jsonify({
            "message": "Połączenie OK!",
            "database": database_address
        })

    except Exception as error:
        db.session.rollback()

        return jsonify({
            "message": "Błąd połączenia z bazą",
            "error": str(error)
        }), 500


# LESSON18_TASK2 – LICZNIK ZAPYTAŃ SQL

# lesson18_task2
query_count = 0
query_counter_started = False


# lesson18_task2
def setup_query_counter():
    """
    Uruchamia licznik zapytań SQL.

    Funkcja powinna zostać wywołana jeden raz
    podczas uruchamiania aplikacji w run.py.
    """

    global query_count
    global query_counter_started

    if query_counter_started:
        return

    @event.listens_for(
        db.engine,
        "before_cursor_execute"
    )
    def count_queries(
        conn,
        cursor,
        statement,
        parameters,
        context,
        executemany
    ):
        global query_count
        query_count += 1

    query_counter_started = True


def reset_queries():
    """
    Zeruje licznik zapytań przed rozpoczęciem pomiaru.
    """

    global query_count
    query_count = 0


# LESSON18_TASK2 – PROBLEM N+1

# lesson18_task2 - bez optymalizacji
@dashboard_bp.route("/debug/n-plus-1")
def n_plus_1():
    """
    Pobiera rezerwacje bez joinedload.

    Dostęp do:
    - booking.room,
    - booking.user

    może powodować wykonywanie dodatkowych zapytań SQL.
    """

    reset_queries()
    start_time = time()

    bookings = Booking.query.all()

    results = []

    for booking in bookings:
        results.append({
            "title": booking.title,
            "room": booking.room.name,
            "user": booking.user.name
        })

    execution_time = time() - start_time

    return jsonify({
        "version": "N+1 – bez optymalizacji",
        "time_seconds": round(execution_time, 4),
        "queries": query_count,
        "items": len(results),
        "results": results
    })


# LESSON18_TASK2 – JOINEDLOAD

# lesson18_task2 - optymalizacja joinedload
@dashboard_bp.route("/debug/n-plus-1-optimized")
def n_plus_1_optimized():
    """
    Pobiera rezerwacje razem z salami i użytkownikami.

    joinedload ogranicza liczbę dodatkowych zapytań SQL.
    """

    reset_queries()
    start_time = time()

    bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).all()

    results = []

    for booking in bookings:
        results.append({
            "title": booking.title,
            "room": booking.room.name,
            "user": booking.user.name
        })

    execution_time = time() - start_time

    return jsonify({
        "version": "OPTIMIZED – joinedload",
        "time_seconds": round(execution_time, 4),
        "queries": query_count,
        "items": len(results),
        "results": results
    })
    
