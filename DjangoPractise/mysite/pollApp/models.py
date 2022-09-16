from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Question(models.Model):
    questions=models.CharField(max_length=100)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    questions=models.ForeignKey(questions,on_delete=CASCADE)
    
