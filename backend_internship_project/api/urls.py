from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("send-sms/", views.send_sms, name="send_sms"),
]