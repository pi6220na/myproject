from django.conf.urls import  include, url
from myapp.views import list, index

from django.urls import path, include
app_name = 'myapp'
urlpatterns = [
    path('', index),

    url(r'^$', list, name='index'),
    url(r'^list/$', list, name='list'),

]

