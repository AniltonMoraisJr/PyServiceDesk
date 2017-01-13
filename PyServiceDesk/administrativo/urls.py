from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.manager, name="manager"),
    url(r'^organizacao/', include('PyServiceDesk.administrativo.organizacao.urls', namespace='organizacao'))
]
