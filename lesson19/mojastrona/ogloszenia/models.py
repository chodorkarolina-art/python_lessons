from django.db import models

#lesson20_task8
from datetime import timedelta
from django.utils import timezone

# Create your models here.

# lesson19_task6
class Ogloszenie(models.Model):
    tytul = models.CharField(max_length=100)
    opis = models.TextField()
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    data_dodania = models.DateTimeField(auto_now_add=True)
    
    # lesson19_task10
    def __str__(self):
        return self.tytul

    class Meta:
        verbose_name = "Ogłoszenie"
        verbose_name_plural = "Ogłoszenia"
        
# lesson20_task8
# lesson21_task1 - model Category został utworzony w lekcji 20 i wykorzystujemy go ponownie
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"
    
# lesson20_task3
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    # lesson20_task8
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    
# lesson20_task6
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    
# lesson21_task7
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    # lesson21_task8
    is_published = models.BooleanField(default=True)

    # lesson21_task8 - data potrzebna do sprawdzenia ostatnich 3 dni
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
