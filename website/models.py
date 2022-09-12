
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Website(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null = False)
    url = models.URLField(max_length=200,null = True)
    waiting_time_before_send = models.IntegerField(null = False)

    def __str__(self):
        return self.name

class Page(models.Model):
    website = models.ForeignKey(Website,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null = False)
    url = models.URLField(max_length=200,null = False)
    
    def __str__(self):
        return self.name

class Page_status_history(models.Model):
    Page = models.ForeignKey(Page,on_delete=models.CASCADE)
    status_code_type = models.CharField(null = False,max_length = 10)
    text = models.TextField(null = True)
    headers = models.TextField(null = True)
    response_time = models.IntegerField(null = False)
    sended_at = models.DateTimeField(auto_now_add=True)
    