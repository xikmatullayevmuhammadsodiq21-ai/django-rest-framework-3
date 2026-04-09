from django.urls import path
from . import views

urlpatterns = [path("myapi/", views.MyAPi.as_view())]
