# lesson22_task7 - seeder kategorii i postów
# lesson22_task9 - rozbudowa seedera o tagi

import random

from django.core.management.base import BaseCommand
from faker import Faker

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = "Usuwa stare dane i tworzy testowe kategorie, tagi oraz posty"

    def handle(self, *args, **options):
        fake = Faker("pl_PL")

        self.stdout.write(
            "Usuwanie istniejących postów, kategorii i tagów..."
        )

        # lesson22_task7 - usuwanie starych postów i kategorii
        Post.objects.all().delete()
        Category.objects.all().delete()

        # lesson22_task9 - usuwanie starych tagów
        Tag.objects.all().delete()

        # lesson22_task7 - predefiniowane kategorie
        category_names = [
            "Technologia",
            "Podróże",
            "Kulinaria",
            "Sport",
            "Kultura",
            "Zdrowie",
            "Nauka",
        ]

        categories = []

        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)

        self.stdout.write(
            self.style.SUCCESS(
                f"Utworzono kategorii: {len(categories)}"
            )
        )

        # lesson22_task9 - predefiniowane tagi
        tag_names = [
            "Python",
            "Django",
            "Backend",
            "Frontend",
            "Bazy danych",
            "Web",
            "Poradnik",
            "Nowości",
            "Programowanie",
            "Technologia",
        ]

        tags = []

        for name in tag_names:
            tag = Tag.objects.create(name=name)
            tags.append(tag)

        self.stdout.write(
            self.style.SUCCESS(
                f"Utworzono tagów: {len(tags)}"
            )
        )

        # lesson22_task7 - tworzenie 100 losowych postów
        # lesson22_task9 - przypisywanie od 1 do 5 tagów
        for _ in range(100):
            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content="\n\n".join(fake.paragraphs(nb=3)),
                category=random.choice(categories),
            )

            number_of_tags = random.randint(1, 5)
            selected_tags = random.sample(
                tags,
                number_of_tags,
            )

            post.tags.add(*selected_tags)

        self.stdout.write(
            self.style.SUCCESS(
                "Utworzono 100 losowych postów."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Każdemu postowi przypisano od 1 do 5 tagów."
            )
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Seedowanie zakończone."
            )
        )