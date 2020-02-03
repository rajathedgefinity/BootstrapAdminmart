from django.contrib import admin
from .models import hubinfo,user_info,loginfo
# Register your models here.

admin.site.register(hubinfo)
admin.site.register(user_info)
admin.site.register(loginfo)
