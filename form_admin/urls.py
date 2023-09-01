
from django.urls import path, include
from . import views

urlpatterns = [
    path('form/<int:form_id>/', views.dynamic_form_view, name='form')
]
