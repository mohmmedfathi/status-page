from django.contrib import admin
from .models import Website,Page,PageHistory
# Register your models here.
admin.site.register(Website)
admin.site.register(Page)
admin.site.register(PageHistory)