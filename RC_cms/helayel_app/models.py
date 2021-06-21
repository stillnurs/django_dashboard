from django.db import models
from django.db.models.aggregates import Count
from django.db.models.deletion import SET_NULL
from django.contrib.auth.models import User
# Create your models here.


class CharityList(models.Model):
    country = models.CharField(max_length=100)
    name = models.CharField(max_length=255)


    def __str__(self):
            return self.title
        
    class Meta:
        verbose_name = 'CharityList'
        verbose_name_plural = 'CharityList'


class Donation(models.Model):
    
    charity_list = models.ForeignKey(CharityList, on_delete=SET_NULL, related_name='donations', null=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, related_name='user_donation', null=True)
    amount = models.DecimalField(decimal_places=4, max_digits=10)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Donation'
        verbose_name_plural = 'Donations'
    
    
class StoryList(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'StoryList'
        verbose_name_plural = 'StoryLists'
    
    

class News(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class FunFact(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'FunFact'
        verbose_name_plural = 'FunFacts'
    
    
class Participates(models.Model):
    
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=SET_NULL, related_name='user_participates', null=True)
    image = models.ImageField()
    approved = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Participates'
        verbose_name_plural = 'Participates'