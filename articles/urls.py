from django.conf.urls import  url
from django.urls import path

from.import views


urlpatterns = [
    url(r'^$', views.article_list),
    url('asd', views.index, name='index'),
]
