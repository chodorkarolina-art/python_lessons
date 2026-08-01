"""
Główny plik uruchamiający aplikację.
"""
from sqlalchemy import inspect
import random
from datetime import datetime, timedelta, timezone

from app import create_app
from app.models import Booking, Equipment, Room, User
from app.db import db

# lesson18_task2
from app.routes.dashboard import setup_query_counter

app = create_app()


EQUIPMENT_DATA = [
    {"name": "Projektor", "icon": "projector"},
    {"name": "Tablica", "icon": "chalkboard"},
    {"name": "Wideokonferencja", "icon": "video"},
    {"name": "Klimatyzacja", "icon": "snowflake"},
    {"name": "Nagłośnienie", "icon": "volume-up"},
]

ROOMS_DATA = [
    {
        "name": "Sala A1",
        "capacity": 10,
        "floor": 1,
        "description": "Mała sala do spotkań zespołowych",
        "hourly_rate": 50,
        "equipment_names": ["Tablica", "Klimatyzacja"]
    },
    {
        "name": "Sala B2",
        "capacity": 20,
        "floor": 2,
        "description": "Średnia sala z projektorem",
        "hourly_rate": 80,
        "equipment_names": ["Projektor", "Wideokonferencja", "Klimatyzacja"]
    },
]

USERS_DATA = [
    {"name": "Jan Kowalski", "email": "jan@firma.pl", "department": "IT", "is_admin": False},
    {"name": "Anna Nowak", "email": "anna@firma.pl", "department": "HR", "is_admin": False},
]

BOOKING_TITLES = [
    "Spotkanie zespołu",
    "Code review",
    "Prezentacja projektu",
]


def seed_database():
    """Wypełnia bazę przykładowymi danymi."""
    with app.app_context():
        if User.query.first():
            return

        equipments_map = {}
        for eq_data in EQUIPMENT_DATA:
            eq = Equipment(name=eq_data["name"], icon=eq_data["icon"])
            db.session.add(eq)
            equipments_map[eq_data["name"]] = eq

        db.session.commit()

        rooms = []
        for room_data in ROOMS_DATA:
            room = Room(
                name=room_data["name"],
                capacity=room_data["capacity"],
                floor=room_data["floor"],
                description=room_data["description"],
                hourly_rate=room_data["hourly_rate"]
            )
            room.equipment = [
                equipments_map[name] for name in room_data["equipment_names"]
            ]
            db.session.add(room)
            rooms.append(room)

        users = []
        for user_data in USERS_DATA:
            user = User(**user_data)
            db.session.add(user)
            users.append(user)

        db.session.commit()

        now = datetime.now(timezone.utc).replace(minute=0, second=0, microsecond=0)

        for _ in range(20):
            room = random.choice(rooms)
            user = random.choice(users)

            start = now + timedelta(days=random.randint(0, 7))
            end = start + timedelta(hours=1)

            if room.is_available(start, end):
                booking = Booking(
                    room_id=room.id,
                    user_id=user.id,
                    title=random.choice(BOOKING_TITLES),
                    start_time=start,
                    end_time=end,
                    attendees_count=2,
                    applied_hourly_rate=room.hourly_rate
                )
                db.session.add(booking)

        db.session.commit()



# START APLIKACJI
if __name__ == "__main__":
    with app.app_context():

        # ZADANIE 2 - aktywacja licznika SQL (N+1 debug)
        setup_query_counter()

        inspector = inspect(db.engine)

        # ZADANIE 1 - inicjalizacja bazy
        if not inspector.has_table("rooms"):
            print("Inicjalizacja nowej bazy danych...")
            db.create_all()
            seed_database()
        else:
            print("Baza danych już istnieje. Aktualizuję schemat...")
            db.create_all()   

    app.run(debug=True, port=5000)