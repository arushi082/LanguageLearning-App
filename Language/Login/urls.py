from django.urls import path, include
from.import views

app_name = "Login"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.user_logout, name="logout"),
    ]
