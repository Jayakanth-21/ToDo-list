from django.db import models

# Create your models here.

class Todo(models.Model):

    date = models.CharField(max_length=25)

    def __str__(self):

        return self.date




