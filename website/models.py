
from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class Website(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL,null = True)
    name = models.CharField(max_length=100,null = False)
    url = models.URLField(max_length=200,null = True)
    waiting_time_before_send = models.IntegerField(null = False)
    
    def __str__(self):
        return self.name

class Page(models.Model):
    website = models.ForeignKey(Website,on_delete=models.SET_NULL,null = True)
    name = models.CharField(max_length=100,null = False)
    url = models.URLField(max_length=200,null = False)
    
    def __str__(self):
        return self.name
    
    

class PageHistory(TimeStampedModel):
    Page = models.ForeignKey(Page,on_delete=models.SET_NULL,null=True)
    satus_code = models.CharField(null = False,max_length = 10)
    text = models.TextField(null = True)
    headers = models.TextField(null = True)
    response_time = models.FloatField(null = False)
    
    