from django.db import models
from django.contrib.auth.models import User
import datetime



class Skills(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subject_photo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    

class Photographer(models.Model):
    info = models.ForeignKey(User,on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skills)
    description = models.TextField()
    image = models.ImageField(upload_to='photographer',default='photographer.jpg')
    status = models.BooleanField(default=False)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.info.username

    
class Services(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='gallery',default='photo.jpg')
    subject_photo= models.ManyToManyField(Subject_photo)
    price = models.IntegerField(default=0)
    client = models.ManyToManyField(Client)
    project_date = models.DateTimeField(default=datetime.datetime.now())
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)   

    class Meta:
        ordering = ('-created_date',)


    def __str__(self):
        return self.title
     

    

class ContactUs(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=220)
    message = models.TextField()

    def __str__(self):
        return self.name
