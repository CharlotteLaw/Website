from django.urls import path, include
from . import views #import views module from current folder, .

#url mapping. mapping root url, '', to view function
urlpatterns = [
    path('', views.project),  #second argument, passing reference to 2nd argument
    path('new/', views.new)
]