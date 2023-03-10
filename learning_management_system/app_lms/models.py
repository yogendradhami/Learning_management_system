from django.db import models

# Create your models here.

# Teacher  Model
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    address  = models.TextField()

    class Meta:
        verbose_name_plural ="1. Teachers"

# Cource Model
class CourceCategory(models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        verbose_name_plural ="2. Cource Categories"

# Cource Model
class Cource(models.Model):
    category = models.ForeignKey(CourceCategory, on_delete=models.CASCADE)
    teacher= models.ForeignKey(Teacher,  on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural ="3. Cources"

# Student Model
class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=20)
    address  = models.TextField()
    interested_categories = models.TextField()

    class Meta:
        verbose_name_plural ="4. Students"