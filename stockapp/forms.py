from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ฟอร์มสำหรับการลงทะเบียน
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ฟอร์มสำหรับการล็อกอิน
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
