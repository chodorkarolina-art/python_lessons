# lesson18_task6

"""
Miesięczny raport PDF rezerwacji.

Endpoint:
GET /api/reports/monthly?month=2026-07
"""

from collections import Counter
from datetime import datetime
from decimal import Decimal
from io import BytesIO
from pathlib import Path

from flask import Blueprint, jsonify, request, send_file

from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from app.models.booking import Booking


# lesson18_task6
reports_bp = Blueprint(
    "reports",
    __name__,
    url_prefix="/api/reports"
)


def register_pdf_fonts():
    """
    Rejestruje czcionkę Arial na Windows,
    żeby polskie znaki poprawnie wyświetlały się w PDF.

    Jeśli Arial nie zostanie znaleziony,
    używana jest standardowa czcionka Helvetica.
    """

    regular_font_path = Path("C:/Windows/Fonts/arial.ttf")
    bold_font_path = Path("C:/Windows/Fonts/arialbd.ttf")

    if regular_font_path.exists() and bold_font_path.exists():
        pdfmetrics.registerFont(
            TTFont("AppFont", str(regular_font_path))
        )

        pdfmetrics.registerFont(
            TTFont("AppFont-Bold", str(bold_font_path))
        )

        return "AppFont", "AppFont-Bold"

    return "Helvetica", "Helvetica-Bold"


def calculate_booking_hours(booking):
    """
    Oblicza czas rezerwacji w godzinach.
    """

    duration = booking.end_time - booking.start_time
    return max(duration.total_seconds() / 3600, 0)


def calculate_booking_revenue(booking):
    """
    Oblicza przychód z jednej rezerwacji.

    Najpierw używa stawki zapisanej w rezerwacji.
    Jeśli jej nie ma, pobiera aktualną stawkę sali.
    """

    hours = calculate_booking_hours(booking)

    hourly_rate = getattr(
        booking,
        "applied_hourly_rate",
        None
    )

    if hourly_rate is None and booking.room:
        hourly_rate = booking.room.hourly_rate

    if hourly_rate is None:
        hourly_rate = Decimal("0")

    return hours * float(hourly_rate)


def create_utilization_chart(room_counts):
    """
    Tworzy wykres słupkowy liczby rezerwacji według sal.
    """

    drawing = Drawing(
        width=480,
        height=260
    )

    chart = VerticalBarChart()

    chart.x = 55
    chart.y = 55
    chart.width = 390
    chart.height = 160

    room_names = [
        room_name
        for room_name, count in room_counts
    ]

    booking_counts = [
        count
        for room_name, count in room_counts
    ]

    chart.data = [
        booking_counts
    ]

    chart.categoryAxis.categoryNames = room_names

    chart.categoryAxis.labels.angle = 25
    chart.categoryAxis.labels.fontSize = 8
    chart.categoryAxis.labels.dy = -15

    chart.valueAxis.valueMin = 0
    chart.valueAxis.valueMax = max(
        booking_counts,
        default=1
    ) + 1

    chart.valueAxis.valueStep = 1

    chart.bars[0].fillColor = colors.HexColor(
        "#667eea"
    )

    drawing.add(chart)

    return drawing


# =========================================================
# lesson18_task6
# RAPORT MIESIĘCZNY PDF
# GET /api/reports/monthly?month=2026-07
# =========================================================

@reports_bp.route("/monthly", methods=["GET"])
def monthly_report():
    """
    Generuje raport PDF dla wskazanego miesiąca.

    Raport zawiera:
    - liczbę rezerwacji,
    - łączny czas,
    - łączny przychód,
    - top 10 sal,
    - top 10 użytkowników,
    - wykres wykorzystania sal.
    """

    month = request.args.get("month")

    if not month:
        return jsonify({
            "error": (
                "Brak parametru month. "
                "Przykład: ?month=2026-07"
            )
        }), 400

    try:
        start_date = datetime.strptime(
            month + "-01",
            "%Y-%m-%d"
        )

    except ValueError:
        return jsonify({
            "error": (
                "Niepoprawny format miesiąca. "
                "Użyj formatu YYYY-MM, np. 2026-07."
            )
        }), 400

    # lesson18_task6 - wyznaczenie następnego miesiąca
    if start_date.month == 12:
        end_date = datetime(
            start_date.year + 1,
            1,
            1
        )

    else:
        end_date = datetime(
            start_date.year,
            start_date.month + 1,
            1
        )

    # lesson18_task6 - pobranie rezerwacji z miesiąca
    bookings = (
        Booking.query
        .filter(
            Booking.start_time >= start_date,
            Booking.start_time < end_date,
            Booking.status == "confirmed"
        )
        .order_by(Booking.start_time)
        .all()
    )

    total_bookings = len(bookings)

    total_hours = sum(
        calculate_booking_hours(booking)
        for booking in bookings
    )

    total_revenue = sum(
        calculate_booking_revenue(booking)
        for booking in bookings
    )

    # lesson18_task6 - statystyki sal
    room_counter = Counter(
        booking.room.name
        for booking in bookings
        if booking.room is not None
    )

    top_rooms = room_counter.most_common(10)

    # lesson18_task6 - statystyki użytkowników
    user_counter = Counter(
        booking.user.name
        for booking in bookings
        if booking.user is not None
    )

    top_users = user_counter.most_common(10)

    # lesson18_task6 - przygotowanie pliku PDF w pamięci
    pdf_buffer = BytesIO()

    document = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=1.5 * cm,
        leftMargin=1.5 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title=f"Raport rezerwacji {month}"
    )

    regular_font, bold_font = register_pdf_fonts()

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontName=bold_font,
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "ReportHeading",
        parent=styles["Heading2"],
        fontName=bold_font,
        fontSize=14,
        leading=18,
        spaceBefore=12,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        "ReportNormal",
        parent=styles["Normal"],
        fontName=regular_font,
        fontSize=10,
        leading=14
    )

    story = []

    story.append(
        Paragraph(
            f"Raport rezerwacji – {month}",
            title_style
        )
    )

    story.append(
        Paragraph(
            (
                f"Zakres raportu: "
                f"{start_date.strftime('%Y-%m-%d')} – "
                f"{end_date.strftime('%Y-%m-%d')}"
            ),
            normal_style
        )
    )

    story.append(
        Spacer(1, 15)
    )

    # lesson18_task6 - podsumowanie
    story.append(
        Paragraph(
            "Podsumowanie",
            heading_style
        )
    )

    summary_data = [
        ["Wskaźnik", "Wartość"],
        ["Liczba rezerwacji", str(total_bookings)],
        ["Łączny czas", f"{total_hours:.2f} h"],
        ["Łączny przychód", f"{total_revenue:.2f} PLN"],
    ]

    summary_table = Table(
        summary_data,
        colWidths=[9 * cm, 7 * cm]
    )

    summary_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#667eea")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                bold_font
            ),
            (
                "FONTNAME",
                (0, 1),
                (-1, -1),
                regular_font
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                7
            ),
        ])
    )

    story.append(summary_table)

    story.append(
        Spacer(1, 20)
    )

    # lesson18_task6 - top 10 sal
    story.append(
        Paragraph(
            "Top 10 sal",
            heading_style
        )
    )

    rooms_data = [
        ["Miejsce", "Sala", "Liczba rezerwacji"]
    ]

    for index, (room_name, count) in enumerate(
        top_rooms,
        start=1
    ):
        rooms_data.append([
            str(index),
            room_name,
            str(count)
        ])

    if len(rooms_data) == 1:
        rooms_data.append([
            "-",
            "Brak danych",
            "0"
        ])

    rooms_table = Table(
        rooms_data,
        colWidths=[2 * cm, 10 * cm, 4 * cm]
    )

    rooms_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#28a745")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                bold_font
            ),
            (
                "FONTNAME",
                (0, 1),
                (-1, -1),
                regular_font
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (0, 0),
                (0, -1),
                "CENTER"
            ),
            (
                "ALIGN",
                (2, 0),
                (2, -1),
                "CENTER"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            ),
        ])
    )

    story.append(rooms_table)

    story.append(
        Spacer(1, 20)
    )

    # lesson18_task6 - top 10 użytkowników
    story.append(
        Paragraph(
            "Top 10 użytkowników",
            heading_style
        )
    )

    users_data = [
        ["Miejsce", "Użytkownik", "Liczba rezerwacji"]
    ]

    for index, (user_name, count) in enumerate(
        top_users,
        start=1
    ):
        users_data.append([
            str(index),
            user_name,
            str(count)
        ])

    if len(users_data) == 1:
        users_data.append([
            "-",
            "Brak danych",
            "0"
        ])

    users_table = Table(
        users_data,
        colWidths=[2 * cm, 10 * cm, 4 * cm]
    )

    users_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#764ba2")
            ),
            (
                "TEXTCOLOR",
                (0, 0),
                (-1, 0),
                colors.white
            ),
            (
                "FONTNAME",
                (0, 0),
                (-1, 0),
                bold_font
            ),
            (
                "FONTNAME",
                (0, 1),
                (-1, -1),
                regular_font
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.grey
            ),
            (
                "ALIGN",
                (0, 0),
                (0, -1),
                "CENTER"
            ),
            (
                "ALIGN",
                (2, 0),
                (2, -1),
                "CENTER"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            ),
        ])
    )

    story.append(users_table)

    # lesson18_task6 - wykres
    if top_rooms:
        story.append(
            PageBreak()
        )

        story.append(
            Paragraph(
                "Wykres wykorzystania sal",
                heading_style
            )
        )

        story.append(
            create_utilization_chart(top_rooms)
        )

    document.build(story)

    pdf_buffer.seek(0)

    filename = (
        f"raport_rezerwacji_{month}.pdf"
    )

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=filename
    )