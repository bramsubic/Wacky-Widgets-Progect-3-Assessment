from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
from django.db.models import Sum

# Create your views here.
def widget_index(request):
  widget_list = Widget.objects.all()
  widget_form = WidgetForm()
  total = widget_list.aggregate(Sum('quantity'))['quantity__sum']
  print(total)
  return render(request, 'index.html', { 'widget_list': widget_list, 'widget_form': widget_form, 'total': total})

def add(request):
    Widget.objects.create(
        description=request.POST['description'],
        quantity=request.POST['quantity'],
    )
    return redirect('/')

def delete(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('/')