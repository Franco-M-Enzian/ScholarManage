from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name="signup"),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login"
        ),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path("<str:username>/profile/", views.ProfileView.as_view(), name="profile"),
]
