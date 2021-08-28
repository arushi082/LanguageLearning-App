from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'name', 'position', 'video', 'ppt', 'Notes')

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
