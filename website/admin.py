from django.contrib import admin
from .models import Website,Page,Page_status_history
# Register your models here.
admin.site.register(Website)
admin.site.register(Page)
admin.site.register(Page_status_history)