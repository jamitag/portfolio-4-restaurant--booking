from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime as dt
from django.core.validators import MaxValueValidator


"""
Returns a default user to ensure the user foreign key is never null
"""

def get_user():
    return User.objects.all()[0]


"""
Model for contact form
"""

# class contact(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     first_name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length=11)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, default=get_user().pk)
#     # def __str__(self):
#     #     return self.first_name


"""
Model for reservations
"""

class Reserve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField(default=dt.time(00, 00))
    parties = models.IntegerField(validators=[MaxValueValidator(50)])
    contact = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return str(self.author) + ": " + str(self.date)