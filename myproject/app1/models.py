from django.db import models


class product(models.Model):
    item=models.CharField(max_length=111)
    store=models.CharField(max_length=500)
    no_item=models.IntegerField()

class Staff(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

class Course(models.Model):
    name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)

class Language(models.Model):
    item=models.CharField(max_length=500)
    description=models.CharField(max_length=500)