from django.urls import path
from . import views


urlpatterns = [
    # lesson22_task3 - strona główna
    path("", views.home, name="home"),

    # lesson22_task2 - lista postów wybranej kategorii
    path(
        "category/<int:category_id>/",
        views.category_posts_view,
        name="category-posts",
    ),
]