
from django.urls import path
from . import views

urlpatterns = [
    path('<int:form_id>/', views.dynamic_form_view, name='form'),
    path('', views.dynamic_form_view, {'form_id': 1}, name='form'),
]
