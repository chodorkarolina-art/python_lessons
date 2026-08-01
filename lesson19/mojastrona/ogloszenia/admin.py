from django.contrib import admin
from .models import Ogloszenie, Product, Note, Category, Article


# zadanie 8 (lekcja 19)
@admin.register(Ogloszenie)
class OgloszenieAdmin(admin.ModelAdmin):
    list_display = ("tytul", "cena", "data_dodania")


# lesson20_task6
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category")


# lesson20_task8
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


# lesson20_task6
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title",)
    

# lesson21_task7
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category")
    
# lesson21_task9 - Personalizacja panelu administratora (szybsze rozwiązanie)
admin.site.site_header = "Panel Administratora Mojej Strony"
admin.site.site_title = "Panel Administratora"
admin.site.index_title = "Witaj w panelu administracyjnym"