from django.shortcuts import render
from .models import Widget

# Create your views here.
def widget_index(request):
  widget_list = Widget.objects.all()
  
  return render(request, 'index.html', { 'widget_list': widget_list })