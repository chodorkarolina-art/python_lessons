from datetime import datetime, timedelta, timezone
from sqlalchemy import func, desc
from ..db import db
from ..models import Room, Booking, User


# Zadanie 1 - podstawowe statystyki dashboardu
def get_booking_statistics(start_date=None, end_date=None):

    base_query = Booking.query.filter(Booking.status != 'cancelled')

    if start_date:
        base_query = base_query.filter(Booking.start_time >= start_date)

    if end_date:
        base_query = base_query.filter(Booking.end_time <= end_date)

    total_bookings = base_query.count()

    room_stats = db.session.query(
        Room.name,
        Booking.start_time,
        Booking.end_time
    ).join(Booking, Room.id == Booking.room_id)\
     .filter(
        Booking.status != 'cancelled',
        Booking.start_time.isnot(None),
        Booking.end_time.isnot(None),
        Booking.end_time > Booking.start_time
     ).all()

    room_hours = {}
    room_counts = {}

    for r in room_stats:
        hours = (r.end_time - r.start_time).total_seconds() / 3600
        room_hours[r.name] = room_hours.get(r.name, 0) + hours
        room_counts[r.name] = room_counts.get(r.name, 0) + 1

    weekday_stats = db.session.query(
        func.extract('dow', Booking.start_time).label('weekday'),
        func.count(Booking.id).label('count')
    ).filter(
        Booking.status != 'cancelled'
    ).group_by('weekday').order_by('weekday').all()

    weekdays = ['Nd', 'Pn', 'Wt', 'Śr', 'Cz', 'Pt', 'Sb']

    return {
        'total_bookings': total_bookings,
        'room_stats': [
            {
                'room': name,
                'bookings': room_counts.get(name, 0),
                'hours': round(hours, 1)
            }
            for name, hours in room_hours.items()
        ],
        'weekday_stats': [
            {
                'day': weekdays[int(w.weekday)],
                'count': w.count
            }
            for w in weekday_stats
        ]
    }


# Zadanie 1 - dane do dashboardu
def get_dashboard_summary():

    now = datetime.now(timezone.utc)
    today_date = now.date()
    month_ago = now - timedelta(days=30)

    stats = {
        'total_rooms': Room.query.filter_by(is_active=True).count(),
        'total_users': User.query.count(),
        'total_bookings': Booking.query.filter_by(status='confirmed').count(),
        'bookings_today': Booking.query.filter(
            func.date(Booking.start_time) == today_date,
            Booking.status == 'confirmed'
        ).count()
    }

    upcoming = Booking.query.options(
        db.joinedload(Booking.room),
        db.joinedload(Booking.user)
    ).filter(
        Booking.start_time >= now,
        Booking.start_time <= now + timedelta(hours=24),
        Booking.status == 'confirmed'
    ).order_by(Booking.start_time).limit(10).all()

    top_users = db.session.query(
        User.name,
        func.count(Booking.id).label('booking_count')
    ).join(Booking).filter(
        Booking.status != 'cancelled'
    ).group_by(User.id).order_by(
        desc('booking_count')
    ).limit(5).all()

    room_stats_query = db.session.query(
        Room.name,
        Booking.start_time,
        Booking.end_time
    ).join(Booking, Room.id == Booking.room_id)\
     .filter(
        Booking.status != 'cancelled',
        Booking.start_time.isnot(None),
        Booking.end_time.isnot(None),
        Booking.end_time > Booking.start_time
     ).all()

    room_hours = {}

    for r in room_stats_query:
        hours = (r.end_time - r.start_time).total_seconds() / 3600
        room_hours[r.name] = room_hours.get(r.name, 0) + hours

    max_hours = 176

    room_utilization = [
        {
            'room': name,
            'hours': round(hours, 1),
            'utilization': round((hours / max_hours) * 100, 2)
        }
        for name, hours in room_hours.items()
    ]

    room_utilization.sort(key=lambda x: x['utilization'], reverse=True)

    return stats, upcoming, top_users, room_utilization


# lesson18_task3
def get_dashboard_api_stats():

    stats = get_booking_statistics()

    department_stats = db.session.query(
        User.department,
        func.count(Booking.id).label("count")
    ).join(Booking).filter(
        Booking.status != 'cancelled'
    ).group_by(User.department).all()

    heatmap = db.session.query(
        func.extract("dow", Booking.start_time).label("day"),
        func.extract("hour", Booking.start_time).label("hour"),
        func.count(Booking.id).label("count")
    ).filter(
        Booking.status != 'cancelled'
    ).group_by("day", "hour").order_by("day", "hour").all()

    month_ago = datetime.now(timezone.utc) - timedelta(days=30)

    trend = db.session.query(
        func.date(Booking.start_time).label("date"),
        func.count(Booking.id).label("count")
    ).filter(
        Booking.start_time >= month_ago
    ).group_by("date").order_by("date").all()

    return {
        "basic_stats": stats,

        "department_stats": [
            {"department": d, "count": c}
            for d, c in department_stats
        ],

        "heatmap": [
            {"day": int(d), "hour": int(h), "count": c}
            for d, h, c in heatmap
        ],

        "trend": [
            {"date": str(date), "count": count}
            for date, count in trend
        ]
    }