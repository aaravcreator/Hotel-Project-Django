from django.db import models

# Create your models here.

class Contact(models.Model):
    #location
    email = models.EmailField()
    contact = models.CharField(max_length = 15)
    message = models.TextField()


    def __str__(self):
        return str(self.id)