from django.urls import path
from . import views

urlpatterns = [
    path("myapi/", views.MyAPi.as_view()),
    path("mashina/", views.MashinaApiView.as_view()),
    path("mashina/<int:pk>/", views.MashinaDetailApiView.as_view()),
]
