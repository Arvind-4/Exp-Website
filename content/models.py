from django.db import models
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class IpAddress(models.Model):
    ip = models.CharField(max_length=255)
    def __str__(self):
        return self.ip



class SubjectList(models.Model):
    subject = models.CharField(max_length=225)
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject)
        return super(SubjectList, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.subject}'


class Category(models.Model):
    category = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.category}'

class Content(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, editable=False)
    content = RichTextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(SubjectList, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    likes = models.ManyToManyField(User, blank=True)
    views = models.ManyToManyField(IpAddress,blank=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Content, self).save(*args, **kwargs)

    def like_count(self):
        return self.likes.count()

    def view_count(self):
        return self.views.count()
