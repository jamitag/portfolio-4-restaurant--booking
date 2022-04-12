from django.db import models

import uuid

class reservation():
    def __init__(self, date, parties, contact):
        self.id = uuid.uuid4()
        self.date = date
        self.parties = parties
        self.contact = contact


class contact():
    def __init__(self, first_name, surname, email, phone_number):
        self.id = uuid.uuid4()
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number


# Create your models here.
