from django.db import models

# Create your models here.
class Place(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class star(models.Model):
    objects = None
    sname=models.CharField(max_length=250)
    simg=models.ImageField(upload_to='pics')
    sdesc=models.TextField()

    def __str__(self):
        return self.sname