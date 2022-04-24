from django.db import models

# Create your models here.
class baikemodel(models.Model):

    title = models.CharField(max_length=10)
    
    ent = models.CharField(max_length=500)

    def __str__(self):
        return self.title + " - " + self.ent


