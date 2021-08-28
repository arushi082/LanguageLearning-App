from django.urls import path, include
from .import views

app_name = "Translate"

urlpatterns = [
    #translate
    path("", views.index, name="index"),
    path("translate/", views.translate, name="translate")
    ]
