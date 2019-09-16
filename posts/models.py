from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(max_length=80)

    text = models.TextField()

    author = models.CharField(max_length=30)

    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.title
    
   
