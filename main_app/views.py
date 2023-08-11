from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Finch, Toy
from .forms import BathingForm

# Create your views here.
def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id = finch_id)
    id_list = finch.toys.all().values_list('id')
    toys_cat_doesnt_have = Toy.objects.exclude(id__in=id_list)
    bathing_form = BathingForm()
    return render(request, 'finches/detail.html', { 
        'finch': finch,
        'bathing_form': bathing_form,
        'toys': toys_cat_doesnt_have
        })

def add_bathing(request, finch_id):
    form = BathingForm(request.POST)
    if form.is_valid():
        new_bathing = form.save(commit=False)
        new_bathing.finch_id = finch_id
        new_bathing.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'type', 'description', 'age']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['type', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'
    
class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'

def assoc_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.add(toy_id)
  return redirect('detail', finch_id=finch_id)

def remove_toy(request, finch_id, toy_id):
  Finch.objects.get(id=finch_id).toys.remove(toy_id)
  return redirect('detail', finch_id=finch_id)