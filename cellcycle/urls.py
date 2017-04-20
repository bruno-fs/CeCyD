from django.conf.urls import include, url

from cellcycle import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]