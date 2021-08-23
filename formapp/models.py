from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    subject = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name