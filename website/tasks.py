from statuspage.celery import app

import requests
from .models import Website
from .models import Page
from .models import Page_status_history
from django.db import connection
from celery import shared_task
from django.contrib.auth.models import User
@shared_task
def task():
    """Perform a calculation & update the status"""
    print('test')
    u = User.objects.filter().first()

    print(Website.objects.all())
    print()
    # test by insert on website
    Website.objects.create(user = u,name = 'last',waiting_time_before_send = '5',url = 'http://xware.co')
    print(Website.objects.all())

    # get page to link page history with it
    x= Page.objects.get()
    if x:
        print('x ok')
    response = requests.get('https://xware.co/') 
    print("status code = " + str(response.status_code))

    
    print('page status history elements : ')
    print(Page_status_history.objects.all())

    # create Page_status_history object
    Page_status_history.objects.create(Page = x,
    status_code_type = response.status_code,
    response_time = 54
    )
    
    print('page status history elements : ')
    print(Page_status_history.objects.all())
   