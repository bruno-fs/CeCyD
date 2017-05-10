from django.conf.urls import url
from django.views.generic import TemplateView

from cellcycle import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
]