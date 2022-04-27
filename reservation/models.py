from django.db import models

import uuid

class reservation(models.Model):
    id = models.UUIDField()
    date = models.DateTimeField()
    parties = models.IntegerField()
    contact = models.ForeignKey(contact, on_delete=models.CASCADE)


class contact():
    def __init__(self, first_name, surname, email, phone_number):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number


# Create your models here.
