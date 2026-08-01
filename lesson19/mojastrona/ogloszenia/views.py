# lesson20_task1
from datetime import timedelta  # lesson21_task8 - obliczanie ostatnich 3 dni

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator  # lesson20_task10
from django.utils import timezone  # lesson21_task8 - aktualna data i czas

from .models import (
    Product,
    Note,
    Category,
    Article,
)  # lesson20_task4, lesson20_task6, lesson21_task3, lesson21_task8

from .forms import ProductForm  # lesson20_task7


def info(request):
    return HttpResponse("Informacje o stronie")


def rules(request):
    return HttpResponse("Regulamin")

# lesson20_task2
def user_profile(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")

# lesson20_task4
def product_list(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, "products.html", context)

# lesson20_task6 - lista wszystkich notatek
# def note_list(request):
#     notes = Note.objects.all()
#
#     context = {
#         "notes": notes
#     }
#
#     return render(request, "notes.html", context)


# lesson20_task10 - lista notatek z paginacją
def note_list(request):
    notes = Note.objects.all().order_by("id")

    paginator = Paginator(notes, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }

    return render(request, "notes.html", context)


# lesson20_task6 - szczegóły jednej notatki
def note_detail(request, note_id):
    note = Note.objects.get(id=note_id)

    context = {
        "note": note
    }

    return render(request, "note_detail.html", context)

# lesson20_task7 - formularz dodawania produktu
from django.shortcuts import redirect


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/products/")

    else:
        form = ProductForm()

    context = {
        "form": form
    }

    return render(request, "add_product.html", context)

# lesson20_task9 - filtrowanie produktów po kategorii

def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)

    context = {
        "products": products
    }

    return render(request, "products.html", context)

# lesson21_task3 - lista wszystkich kategorii
def category_list(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }

    return render(request, "categories.html", context)

# lesson21_task6 - szczegóły jednej kategorii
def category_detail_view(request, pk):

    category = Category.objects.get(id=pk)

    context = {
        "category": category
    }

    return render(request, "category_detail.html", context)

# lesson21_task8 - lista opublikowanych artykułów
# def article_list_view(request):

#     articles = Article.objects.filter(is_published=True)

#     context = {
#         "articles": articles
#     }

#     return render(request, "article_list.html", context)


# lesson21_task10 - wyszukiwanie artykułów
def article_list_view(request):
    articles = Article.objects.filter(is_published=True)

    query = request.GET.get("q")

    if query:
        articles = articles.filter(title__icontains=query)

    three_days_ago = timezone.now() - timedelta(days=3)

    article_data = []

    for article in articles:
        article_data.append({
            "article": article,
            "is_new": article.published_at >= three_days_ago
        })

    context = {
        "article_data": article_data,
        "query": query
    }

    return render(request, "article_list.html", context)