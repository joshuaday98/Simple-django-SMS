from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_page, name='post_page'),
]
