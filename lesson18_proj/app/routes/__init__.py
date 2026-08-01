from .booking import bookings_bp
from .dashboard import dashboard_bp
from .equipment import equipment_bp
from .rooms import rooms_bp

# lesson18_task4
from .notifications import notifications_bp

# lesson18_task5
from .series import series_bp

# lesson18_task6
from .reports import reports_bp


BLUEPRINTS = [
    bookings_bp,
    dashboard_bp,
    equipment_bp,
    rooms_bp,
    notifications_bp,
    series_bp,
    reports_bp
]

# lesson18_task4
from .notifications import notifications_bp

# lesson18_task5
from .series import series_bp

# lesson18_task6
from .reports import reports_bp


def register_blueprints(app):
    app.register_blueprint(rooms_bp)
    app.register_blueprint(bookings_bp)

    # lesson18_task1, lesson18_task2, lesson18_task3
    app.register_blueprint(dashboard_bp)

    app.register_blueprint(equipment_bp)

    # lesson18_task4
    app.register_blueprint(notifications_bp)

    # lesson18_task5
    app.register_blueprint(series_bp)

    # lesson18_task6
    app.register_blueprint(reports_bp)

