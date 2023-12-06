from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from WebDocumentTracker import views


urlpatterns = [
     path('', views.index, name='home'),
     path('login/', views.CustomLoginView.as_view(), name='login'),
     path('about/', views.about, name='about'),
     # path('user_profile/<int:pk>/', views.ShowProfilePageView.as_view(), name='user_profile'),
     path('user/', views.userpage, name = 'userpage'),
     path('create_profile_page/', views.CreateProfilePageView.as_view(), name='create_user_profile'),
     path('edit_profile/', views.UserEditView.as_view(), name='edit_user_profile'),
     path('logout/', views.logoutMethod, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)