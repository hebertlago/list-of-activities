from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL de login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL de logout
]