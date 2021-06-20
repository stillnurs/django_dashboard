from django.db import models


class Person(models.Model):
    
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    
    class Meta:
        
        def __str__(self) -> str:
            return self.username
            