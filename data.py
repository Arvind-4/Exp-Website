import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

import django

django.setup()

from django.db import transaction
from faker import Faker
from content.models import Content, Category, SubjectList

fake = Faker()


@transaction.atomic
def create_subjects():
    models = [Content, Category, SubjectList]
    for m in models:
        m.objects.all().delete()
    for k in range(100):
        content = Content.objects.create(
            title=fake.name(),
            content=fake.text(),
            subject=SubjectList.objects.create(subject=fake.name()),
        )
        content.save()
        Category.objects.create(category=fake.name())
    return True


create_subjects()
