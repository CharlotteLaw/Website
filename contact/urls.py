from django.urls import path
from . import views

#url mapping. mapping root url, '', to view function
urlpatterns = [
    path('', views.contact)
]