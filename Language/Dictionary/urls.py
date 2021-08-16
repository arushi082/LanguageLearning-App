from django.urls import path, include
from.import views

app_name = "dictionary"

urlpatterns = [
    #dictionary-page
    path("", views.dictionary, name="dictionary"),

    ]
