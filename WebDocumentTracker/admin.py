from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
from django.conf import settings
from django.contrib import admin

admin.site.site_header = "Web Document Tracker"
admin.site.site_title = "Панель администрирования"
admin.site.index_title = "Добро пожаловать в админку"