
from django.urls import path, include
from . import views

urlpatterns = [
    path('form', views.dynamic_form_view)
]
