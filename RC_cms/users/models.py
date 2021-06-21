from django.db import models
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    total_points = models.IntegerField(("Total Points"))
    total_donation = models.DecimalField(("Total Donations"), decimal_places=4, max_digits=1000)
    
    def __str__(self):
            return self.username
        
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    

class Employee(models.Model):
    
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    
    designition = models.CharField(max_length=50)
    
    def __str__(self):
            return self.username
        
    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
    


class Designition(models.Model):
    
    title = models.CharField(max_length=50)
    user = models.ForeignKey(Employee, on_delete=SET_NULL, related_name='designitions', null=True)
    
    
    def __str__(self):
            return self.username
        
    class Meta:
        verbose_name = 'Designition'
        verbose_name_plural = 'Designitions'
        
        
