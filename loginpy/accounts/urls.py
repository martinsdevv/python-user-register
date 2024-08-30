from django.urls import path
from .views import register, user_login, main_page, reset_password_basic

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('main/', main_page, name='main'),
    path('reset_password/', reset_password_basic, name='reset_password_basic'),
]
