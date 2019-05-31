from django.urls import path

from . import views

app_name = 'get_code'
urlpatterns = [
    path('secret/', views.secret, name='secret'),
    path('health/', views.health, name='health'),
]