from django.urls import path
from . import views 

urlpatterns = [
    path('', views.widget_index, name="index"),
]