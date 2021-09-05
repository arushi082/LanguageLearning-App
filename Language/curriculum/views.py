from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                  ListView, CreateView,
                                  UpdateView, DeleteView, FormView, )
from .models import Standard, Subject, Lesson


class StandardListView(ListView):
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'
