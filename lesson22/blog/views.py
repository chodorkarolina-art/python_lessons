from django.shortcuts import render
from .models import Category, Post
from django.db.models import Q  # lesson22_task6 - wyszukiwanie po wielu polach

# lesson22_task2 - lista postów z wybranej kategorii
def category_posts_view(request, category_id):
    category = Category.objects.get(id=category_id)

    posts = Post.objects.filter(category_id=category_id)

    context = {
        "category": category,
        "posts": posts,
    }

    return render(request, "blog/category_posts.html", context)


# lesson22_task3 - strona główna z 5 najnowszymi postami
# lesson22_task6 - wyszukiwarka postów
def home(request):

    posts = Post.objects.order_by("-created_at")

    query = request.GET.get("q")

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    posts = posts[:5]

    context = {
        "posts": posts,
        "query": query,
    }

    return render(request, "blog/home.html", context)
