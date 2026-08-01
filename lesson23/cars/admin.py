from django.contrib import admin, messages
from django.utils.html import format_html

from .models import Car, Dealer


# lesson23_task10 - samochody przypisane do dealera
class CarInline(admin.TabularInline):
    model = Car
    extra = 0


# lesson23_task2 - konfiguracja listy samochodów w panelu admina
# lesson23_task3 - wyszukiwanie po marce i modelu
# lesson23_task4 - filtrowanie po dostępności i roku
# lesson23_task5 - domyślne sortowanie po roku
# lesson23_task6 - niestandardowa kolumna "Pełna nazwa"
# lesson23_task7 - pole year tylko do odczytu
# lesson23_task8 - akcja oznaczająca auta jako niedostępne
# lesson23_task9 - wyświetlanie miniaturki zdjęcia
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "display_photo",
        "full_name",
        "brand",
        "model",
        "year",
        "is_available",
    )

    search_fields = (
        "brand",
        "model",
    )

    list_filter = (
        "is_available",
        "year",
    )

    ordering = (
        "-year",
    )

    readonly_fields = (
        "year",
    )

    actions = (
        "mark_as_unavailable",
    )

    # lesson23_task6 - połączenie marki i modelu
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"

    full_name.short_description = "Pełna nazwa"

    # lesson23_task8 - oznaczenie zaznaczonych aut jako niedostępne
    def mark_as_unavailable(self, request, queryset):
        updated_count = queryset.update(is_available=False)

        self.message_user(
            request,
            f"Oznaczono jako niedostępne: {updated_count} samochodów.",
            messages.SUCCESS,
        )

    mark_as_unavailable.short_description = "Oznacz jako niedostępne"

    # lesson23_task9 - miniaturka zdjęcia
    def display_photo(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="150" />',
                obj.photo.url,
            )

        return "Brak zdjęcia"

    display_photo.short_description = "Zdjęcie"


# lesson23_task10 - dealer i lista przypisanych samochodów
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
    )

    inlines = [
        CarInline,
    ]