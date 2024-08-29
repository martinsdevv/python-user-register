from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  # Adicione esta linha
    path('main/', views.main_page, name='main_page'),
]
