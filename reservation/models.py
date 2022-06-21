from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime as dt
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField


class Menu(models.Model):
    name = models.CharField(max_length=250)
    image = CloudinaryField("Image", resource_type="auto",)

class AboutUs(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    image = CloudinaryField("Image", resource_type="auto",)

class bgImage(models.Model):
    image = CloudinaryField("Image", resource_type="auto")
    

"""
Returns a default user to ensure the user foreign key is never null
"""


def get_user():
    return User.objects.all()[0]


"""
Model for reservations
"""


class Reserve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField(default=dt.time(00, 00))
    parties = models.IntegerField(validators=[MaxValueValidator(50)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.author) + ": " + str(self.date)
