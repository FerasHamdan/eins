from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=15)


    def __str__(self):
        return self.name

class Articale(models.Model):
    title=models.CharField(max_length=16) 
    person=models.ForeignKey(Person,on_delete=models.CASCADE,related_name='articales')


    def __str__(self):
        return self.title

