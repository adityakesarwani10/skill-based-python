from django.db import models

class Member(models.Model):
    universityrollno=models.IntegerField(unique=True)
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)

class MyTable(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)  
