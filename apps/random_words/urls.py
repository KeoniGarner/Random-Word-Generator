from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^reset/$', views.reset),
    re_path(r'^generate/$', views.generate)
]