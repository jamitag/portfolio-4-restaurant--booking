from django.db import models
import uuid
from django.contrib.auth.models import User


def get_user():
    return User.objects.all()[0]


class contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_user().pk)


class reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    parties = models.IntegerField()
    contact = models.ForeignKey(contact, on_delete=models.CASCADE)

