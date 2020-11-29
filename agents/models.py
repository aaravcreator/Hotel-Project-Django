from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    image = models.ImageField(upload_to ='agents/')


    def __str__ (self):
        return self.name
        


