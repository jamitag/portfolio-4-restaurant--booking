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
Model for reservations
"""


class Reserve(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    time = models.TimeField(default=dt.time(00, 00))
    # time = models.CharField(max_length=250, blank=True, null=True)
    parties = models.IntegerField(validators=[MaxValueValidator(50)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.author) + ": " + str(self.date)
