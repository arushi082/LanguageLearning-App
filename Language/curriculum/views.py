from django.views.generic import (TemplateView, DetailView,
                                  ListView, CreateView,
                                  UpdateView, DeleteView, FormView, )

from .models import Languages, Lesson
from django.urls import reverse_lazy
from .forms import LessonForm
from django.http import HttpResponseRedirect


class LanguagesListView(ListView):
    context_object_name = 'languages'
    model = Languages
    template_name = 'curriculum/languages_list_view.html'


class LessonListView(DetailView):
    context_object_name = 'lessons'
    model = Languages
    template_name = 'curriculum/lesson_list_view.html'


class LessonDetailView(DetailView, FormView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'

    def get_success_url(self):
        self.object = self.get_object()
        standard = self.object.Standard
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_detail', kwargs={'languages': standard.slug,
                                                                'lesson': subject.slug,
                                                                'slug': self.object.slug})

    def form_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.lesson_name = self.object.comments.name
        fm.lesson_name_id = self.object.id
        fm.save()
        return HttpResponseRedirect(self.get_success_url())

    def form2_valid(self, form):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.author = self.request.user
        fm.comment_name_id = self.request.POST.get('comment.id')
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonCreateView(CreateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = LessonForm
    context_object_name = 'subject'
    model = Languages
    template_name = 'curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        languages = self.object.languages
        return reverse_lazy('curriculum:lesson_list', kwargs={'languages': languages.slug,
                                                              'slug': self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.languages = self.object.languages
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonUpdateView(UpdateView):
    fields = ('name', 'position', 'video', 'ppt', 'Notes')
    model = Lesson
    template_name = 'curriculum/lesson_update.html'
    context_object_name = 'lessons'


class LessonDeleteView(DeleteView):
    model = Lesson
    context_object_name = 'lessons'
    template_name = 'curriculum/lesson_delete.html'

    def get_success_url(self):
        print(self.object)
        languages = self.object.languages
        lesson = self.object.lesson
        return reverse_lazy('curriculum:lesson_list', kwargs={'standard': languages.slug, 'slug': lesson.slug})
from django.shortcuts import render

# Create your views here.
