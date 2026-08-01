from django.contrib import admin
from .models import Category, Post


# lesson22_task2 - rejestracja modeli do dodania danych testowych
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


# lesson22_task2 - rejestracja postów
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at")