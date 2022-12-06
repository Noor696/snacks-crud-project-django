from django.shortcuts import render
from django.views.generic import TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy  # reverse_lazy wait me until i delete or update after that take me to a specific path

# Create your views here.
class HomePage(TemplateView): 
    ''' responsiple show user the templete'''
    template_name='home.html'

class SnackListView(ListView): 
    template_name='snack_list.html'
    # give it the model we want to show
    model = Snack # the table we want take the data from. 

    # if we want change name of {object list}
    context_object_name = "AllSnacks"

class SnackDetailView(DetailView): 
    template_name='snack_detail.html'
    # give it the model we want to show
    model = Snack # the table we want take the data from. 

class SnackCreateView(CreateView): 
    template_name='snack_create.html'
    model = Snack 
    fields = ['name' , 'img_url' , 'amount', 'description' , 'purchaser']

class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model = Snack 
    fields = ['name' , 'img_url' , 'amount', 'description' , 'purchaser'] # we can remove any fileld we didn't want updated

class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snacks')
