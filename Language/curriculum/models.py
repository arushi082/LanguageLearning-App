from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os

def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.subject_id:
        filename = 'Languages_Pictures/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)



class Languages(models.Model):
    language_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to=save_subject_image, blank=True, verbose_name='Language Image')
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.language_id)
        super().save(*args, **kwargs)



def save_lesson_files(instance, filename):
            upload_to = 'Images/'
            ext = filename.split('.')[-1]
        # get filename
            if instance.lesson_id:
                filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id, instance.lesson_id, ext)
                if os.path.exists(filename):
                    new_name = str(instance.lesson_id) + str('1')
                    filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id, new_name, ext)
                return os.path.join(upload_to, filename)

class Lesson(models.Model):
        lesson_id = models.CharField(max_length=100, unique=True)
        created_by = models.ForeignKey(User, on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        language = models.ForeignKey(Languages, on_delete=models.CASCADE, related_name='lessons')
        name = models.CharField(max_length=250)
        position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
        slug = models.SlugField(null=True, blank=True)
        video = models.FileField(upload_to=save_lesson_files, verbose_name="Video", blank=True, null=True)
        ppt = models.FileField(upload_to=save_lesson_files, verbose_name="Presentations", blank=True)
        Notes = models.FileField(upload_to=save_lesson_files, verbose_name="Notes", blank=True)

        class Meta:
            ordering = ['position']

        def __str__(self):
            return self.name

        def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super().save(*args, **kwargs)

        def get_absolute_url(self):
            return reverse('curriculum:lesson_list', kwargs={'slug': self.lesson.slug, 'standard': self.languages.slug})

# Create your models here.
