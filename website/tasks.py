from statuspage.celery import app
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import requests
from .models import Page
from .models import PageHistory
from statuspage import settings
from celery import shared_task
from django.contrib.auth.models import User
import requests

@shared_task
def task():
    print('test')

    queryset = Page.objects.all()
    for i in queryset:
        #name_of_page = i.name
        url_of_page = i.url
        response = requests.get(url = url_of_page) 

        PageHistory.objects.create(
                     Page = i,
                     satus_code = response.status_code,
                     text = response.text,
                     headers = response.headers,
                     response_time = response.elapsed.total_seconds()
         )

# @shared_task(bind=True)
# def send_mail_func(self):
#     users = get_user_model().objects.all()
#     #timezone.localtime(users.date_time) + timedelta(days=2)
#     for user in users:
#         mail_subject = "Hi! Celery Testing"
#         message = "If you are liking my content, please hit the like button and do subscribe to my channel"
#         to_email = user.email
#         send_mail(
#             subject = mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=True,
#         )
#     return "Done"