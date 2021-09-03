from django.urls import path
from . import views

app_name='curriculum'
urlpatterns = [
    path('', views.LanguagesListView.as_view(), name='language_list'),
    #path('<slug:slug>/',views.LessonListView.as_view(),name='lesson_list'),
]