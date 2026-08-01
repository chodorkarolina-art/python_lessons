"""
URL configuration for mojastrona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ogloszenia import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # lesson20_task1
    path("info/", views.info),
    path("rules/", views.rules),

    # lesson20_task2
    path("user/<str:username>/", views.user_profile),

    # lesson20_task4
    path("products/", views.product_list),
    
    # lesson20_task7
    path("products/add/", views.add_product),

    # lesson20_task6
    path("notes/", views.note_list),
    path("note/<int:note_id>/", views.note_detail),
    
        # lesson20_task9
    path("category/<int:category_id>/", views.products_by_category),
    
    # lesson21_task3
    path("categories/", views.category_list),

    # lesson21_task6
    path("categories/<int:pk>/", views.category_detail_view),
    
    # lesson21_task8
    # lesson21_task10
    path("articles/", views.article_list_view),
] 

