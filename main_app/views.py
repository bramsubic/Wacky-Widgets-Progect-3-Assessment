from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def widget_index(request):
  widget_list = Widget.objects.all()
  widget_form = WidgetForm()
  return render(request, 'index.html', { 'widget_list': widget_list, 'widget_form': widget_form})

def add(request):
    Widget.objects.create(
        description=request.POST['description'],
        quantity=request.POST['quantity'],
    )
    return redirect('/')