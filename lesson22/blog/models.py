from django.db import models


# lesson22_task1 - model kategorii
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


# lesson22_task8 - model tagu
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# lesson22_task1 - model posta przypisanego do kategorii
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    # lesson22_task8 - jeden post może mieć wiele tagów
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    # lesson22_task3 - data potrzebna do sortowania postów
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  
