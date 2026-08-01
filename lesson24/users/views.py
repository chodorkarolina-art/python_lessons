from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import UserRegisterForm, UserUpdateForm


# lesson24_task6
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            # lesson24_task9
            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Konto zostało utworzone i zostałeś automatycznie zalogowany."
        )

        return redirect("home")
    
    else:
        form = UserRegisterForm()

    return render(
        request,
        "users/register.html",
        {"form": form},
    )


# lesson24_task5
@login_required
def home(request):
    return render(request, "users/home.html")


# lesson24_extra_profile_update
@login_required
def profile_update(request):
    if request.method == "POST":
        form = UserUpdateForm(
            request.POST,
            instance=request.user,
        )

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Profil został zaktualizowany."
            )
            return redirect("profile")
    else:
        form = UserUpdateForm(instance=request.user)

    return render(
        request,
        "users/profile_update.html",
        {"form": form},
    )

# lesson24_task10
@staff_member_required
def users_list(request):
    users = User.objects.all()

    return render(
        request,
        "users/users_list.html",
        {"users": users},
    )
    
# lesson24_task3
@login_required
def profile(request):
    return render(request, "users/profile.html")