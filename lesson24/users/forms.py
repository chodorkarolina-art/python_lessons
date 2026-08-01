from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# lesson24_task6
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        
# lesson24_extra_profile_update
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]