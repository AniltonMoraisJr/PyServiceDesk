from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.familyservice, name="familyservice"),
    url(r'^new/$', views.new_familyservice, name="new_familyservice"),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.detail_familyservice, name="detail_familyservice"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit_familyservice, name="edit_familyservice"),
]
