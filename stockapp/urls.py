from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  # หน้าแรก (Home page)
    path('login/', views.login_view, name='login'),  # หน้า Login
    path('register/', views.register_view, name='register'),  # หน้า Register 
]