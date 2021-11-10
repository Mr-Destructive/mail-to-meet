from django.db import models

class Mail(models.Model):

    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    subject = models.CharField(max_length=256)
    body = models.CharField(max_length=384000)
    reciever = models.EmailField(max_length=64)

    def __str__(self):
        return self.subject
