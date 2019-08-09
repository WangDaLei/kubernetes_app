from django.conf.urls import url
# from django.urls import path
from helloworld import views as local_views

urlpatterns = [
    url(r'^system/$', local_views.TestView.as_view(), name='test'),
]
