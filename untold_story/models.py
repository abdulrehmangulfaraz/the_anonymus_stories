from django.db import models

# Create your models here.
class Data(models.Model):
    username = models.CharField(max_length=100)
    data = models.TextField()

    def __str__(self):
        return self.username