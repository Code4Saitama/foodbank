from django.conf.urls import url
from . import views

urlpatterns = [
    url('request', views.request_index, name='request_template'),
    url('timeline', views.timeline_index, name='timeline_template'),
]