from django.urls import path

from . import views

urlpatterns = [
    path('', views.secret, name='secret'),
]