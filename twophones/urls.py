from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.phones_home, name='phones_home'),
]