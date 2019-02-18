from django import forms
from django.contrib.auth.models import User
from user_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ("first_name","last_name","username","password","email",)

class UserUpdateInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('profile_picture',)