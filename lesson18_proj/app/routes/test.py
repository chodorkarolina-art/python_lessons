from flask import Blueprint
from datetime import datetime, timedelta, timezone
from app.db import db
from app.models import Booking

test_bp = Blueprint("test", __name__)


@test_bp.route("/test-booking")
def test_booking():
    b = Booking(
        room_id=1,
        user_id=1,
        title="TEST",
        start_time=datetime.now(timezone.utc) + timedelta(hours=2),
        end_time=datetime.now(timezone.utc) + timedelta(hours=3),
        applied_hourly_rate=50
    )

    db.session.add(b)
    db.session.commit()

    return "OK"