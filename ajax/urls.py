from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)$', views.update_like, name='update_post'),
    url(r'^ajax/(?P<id>\d+)$', views.add_ajax),
]
