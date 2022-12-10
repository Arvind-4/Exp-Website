from django.contrib import admin

# Register your models here.

from .models import (
    Category,
    SubjectList,
    Content
)

admin.site.register(Category)
admin.site.register(SubjectList)
admin.site.register(Content)