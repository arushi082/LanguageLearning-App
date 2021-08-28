from django.urls import path, include
from .import views

app_name = "Translate"

urlpatterns = [
    #translate
    path("", views.index, name="index"),
    path("translate/", views.translate, name="translate")
    ]


"""
app_name = "Dictionary"

urlpatterns = [
    #dictionary-page
    path("", views.index, name="index"),
    path("dictionary/", views.dictionary, name="dictionary")
    ]

"""
