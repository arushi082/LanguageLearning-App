from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView,
                                  ListView)
from .models import Standard, Subject, Lesson
from Logging.logger import AppLogger

logger = AppLogger()


class StandardListView(ListView):
    """
    This class uses django views that are:-
    Django views are a key component of applications built with the framework. At their simplest they are a Python function or class that takes a web request and return a web response. Views are used to do things like fetch objects from the database, modify those objects if needed, render forms, return HTML
    """
    file_object = open("Curriculum_log.txt", 'a+')
    logger.log(file_object, 'Initiating standards model i.e creates the standard table inn sqlite database', 'Info')
    context_object_name = 'standards'
    model = Standard
    template_name = 'curriculum/standard_list_view.html'

class SubjectListView(DetailView):
    """
    creates the details of the subjects that are present in sqlite database using detail view of django list view
    """
    context_object_name = 'standards'
    file_object = open("Curriculum_log.txt", 'a+')
    logger.log(file_object, 'Shows the details of subjects ', 'Info')
    model = Standard
    template_name = 'curriculum/subject_list_view.html'

class LessonListView(DetailView):
    """
    creates the lesson list view using detail view of django list view
    """
    context_object_name = 'subjects'
    file_object = open("Curriculum_log.txt", 'a+')
    logger.log(file_object, 'Shows the name of the lessons of particuluar subject ', 'Info')
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'
    file_object.close()

class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'

