from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=20)

class Eomployee(models.Model):
    fullName=models.CharField(max_length=100)
    phoneNumber=models.CharField(max_length=20)
    empCode=models.CharField(max_length=3)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)