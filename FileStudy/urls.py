from django.conf.urls import url
from FileStudy import views

urlpatterns = [
    url(r'^hello_world/$', views.hello_world),
    url(r'^index/$', views.index),
    url(r'^upload_file/$', views.upload_file, name="upload_file"),
    url(r'^image_upload/$', views.image_upload, name="image_upload"),
    url(r'^mine/$', views.mine, name="mine")
]
