from django.urls import path
from . import views 

urlpatterns = [
    path('', views.widget_index, name="index"),
    path('add/', views.add),
    path('<int:widget_id>/delete/', views.delete),
]