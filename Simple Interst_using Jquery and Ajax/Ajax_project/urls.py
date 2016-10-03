
from django.conf.urls import patterns,include,url
from django.contrib import admin
from simpleinterest.views import home,compute

urlpatterns = [
    url(r'^$',home),
    url(r'^user/compute/$',compute),
]
