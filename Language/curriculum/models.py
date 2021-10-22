from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User
import os
from Logging.logger import AppLogger

logger = AppLogger()


class Standard(models.Model):
    """
    creating table standard model which stores name , slug and desciption of standards . for instance we have used basic and fundamentals as standard
    Slug :- is a short word that is used in creating url's for dynamic website in django
    """
    file_object = open("Curriculum_model_log.txt", 'a+')
    logger.log(file_object, 'Creating table called standard ', 'Info')
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name
        logger.log(file_object, 'name is saved in table ', 'Info')

    def save(self, *args, **kwargs):
        file_object = open("Curriculum_model_log.txt", 'a+')
        self.slug = slugify(self.name)
        logger.log(file_object, 'slug is saved in table ', 'Info')
        super().save(*args, **kwargs)

def save_subject_image(instance, filename):

    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.subject_id:
        filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)

class Subject(models.Model):
    """
    This class creates the subjects table which stores the following information it also using standard table as a foregin key . for example
    in basic standard it will have 2 3 subjects , in fundamental it will have 2 3 subjects
    """
    subject_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE, related_name='subjects')
    image = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=500,blank=True)
    file_object = open("Curriculum_model_log.txt", 'a+')
    logger.log(file_object, 'Created subject table ', 'Info')

    def __str__(self):
        return self.name
        logger.log(file_object, 'name is saved in  subject table ', 'Info')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)
        file_object = open("Curriculum_model_log.txt", 'a+')
        logger.log(file_object, 'slug is saved in subject table ', 'Info')


def save_lesson_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.lesson_id:
        filename = 'lesson_files/{}/{}.{}'.format(instance.lesson_id,instance.lesson_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename =  'lesson_images/{}/{}.{}'.format(instance.lesson_id,new_name, ext)
    return os.path.join(upload_to, filename)

class Lesson(models.Model):
    """
    This class creates table lesson which has follwing attributes  also uses table standard and subject as foreign keys
    """
    lesson_id = models.CharField(max_length=100, unique=True)
    Standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='lessons')
    name = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
    slug = models.SlugField(null=True, blank=True)
    video = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=500,blank=True)
    file_object = open("Curriculum_model_log.txt", 'a+')
    logger.log(file_object, 'Created lesson table ', 'Info')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Generates the url using the slug from both tables
        """
        return reverse('curriculum:lesson_list', kwargs={'slug':self.subject.slug, 'standard':self.Standard.slug})
        file_object = open("Curriculum_model_log.txt", 'a+')
        logger.log(file_object, 'url generated using slugs ', 'Info'
        file_object.close()
# Create your models here.
