from django.db import models


# lesson23_task10 - model dealera
class Dealer(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


# lesson23 - model Car potrzebny do zadań 1-10
class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    photo = models.ImageField(upload_to="cars/")
    owner_website = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)

    # lesson23_task10 - samochód należy do jednego dealera
    dealer = models.ForeignKey(
        Dealer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.brand} {self.model}"