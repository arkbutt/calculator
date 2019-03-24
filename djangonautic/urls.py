from django.contrib import admin
from django.conf.urls import  url,include

from.import views

# urlpatterns = [
#     path('admin/$', admin.site.urls),
#     path('about/$', views.about),
#     path('$', views.homepage),
# ]

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^articles/', include("articles.urls")),
    url(r'^about', views.about),
    url(r'^$', views.homepage),
]
