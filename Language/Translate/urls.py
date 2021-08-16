from django.urls import path, include
from .import views

app_name = "Translate"

urlpatterns = [
    #translate
    path("", views.translate, name="translate"),
    ]
