from time import time
import uuid
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, IntegerField, ImageField, EmailField, ForeignKey, CASCADE, TextField, \
    UUIDField

from apps.task import task_send_email


class User(AbstractUser):
    uuid = UUIDField(editable=False, default=uuid.uuid4, unique=True)
    username = CharField(unique=True,max_length=255)


class Category(Model):
    uuid = UUIDField(editable=False, default=uuid.uuid4, unique=True)
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    uuid = UUIDField(editable=False, default=uuid.uuid4, unique=True)
    name = CharField(max_length=255)
    image = ImageField(upload_to='products/')
    dimensions = CharField(max_length=255)
    version = CharField(max_length=255)
    color = CharField(max_length=255)
    description = TextField()
    email = EmailField()
    price = IntegerField()
    category = ForeignKey('apps.Category', CASCADE)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.id is not None:
            super().save(force_insert, force_update, using, update_fields)
            emails: list = Product.objects.values_list('email', flat=True)
            start = time().time()
            task_send_email.delay('Yangi blog', self.name, list(emails))
            end = time.time()
            print(end - start, '--yuborildi')
        print('yuborilmadi')

    def __str__(self):
        return self.name
