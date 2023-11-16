from django.contrib import admin
from django.urls import path
from WebDocumentTracker import views

urlpatterns = [
    path('', views.auth, name='auth')
]