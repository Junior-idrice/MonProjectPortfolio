from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=123)
    email = models.EmailField()
    text = models.TextField(max_length=320)

    def __str__(self):
        return f"{self.name} - {self.email}"