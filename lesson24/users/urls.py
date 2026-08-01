from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    # lesson24_task5
    path("", views.home, name="home"),

    # lesson24_task6
    path("register/", views.register, name="register"),

    # lesson24_extra_profile_update
    path("profile/update/", views.profile_update, name="profile_update"),

    # lesson24_task8
    path(
        "password-change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),

    # lesson24_task8
    path(
        "password-change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),

    # lesson24_task10
    path("users/", views.users_list, name="users_list"),

    # lesson24_task3
    path("profile/", views.profile, name="profile"),
]