from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from .models import Item

class ItemListView(ListView):
    model = Item
    context_object_name = 'items'
    # You can add additional queryset or context data if needed.

class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'

class ItemCreateView(CreateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('base:itemlist')

class ItemUpdateView(UpdateView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('base:itemlist')
    
class ItemDelete(DeleteView):
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('base:itemlist')