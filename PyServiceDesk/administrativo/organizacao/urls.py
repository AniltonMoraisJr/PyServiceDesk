from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.organization, name="organization"),
    url(r'^new/$', views.new_organization, name="new_organization"),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.detail_organization, name="detail_organization"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_organization, name="edit_organization"),
]
