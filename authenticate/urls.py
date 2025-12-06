from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name = "signup"),
    path('login', views.LoginView, name = "login"),
    path('logout', views.LogoutView, name = "logout"),
    path('forget-password', views.forget_password, name = "forget_password"),
    path('password-reset-sent/<str:reset_id>', views.password_reset_sent, name = "password_reset_sent"),
    path('reset-password/<str:reset_id>', views.reset_password, name = "reset_password"),
]