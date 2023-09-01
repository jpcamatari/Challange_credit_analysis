
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dynamic_form_view, name='form')
]
