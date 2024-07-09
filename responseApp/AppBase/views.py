from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import ListView,DetailView, FormView, CreateView
from .models import Tovar,Tags
from .forms import ResponseForm, CreateTovarForm 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(ListView):
    template_name = 'AppBase/home.html'
    paginate_by = 10
    context_object_name = 'tovar'
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["tovar"] = self.model.objects.select_related('user').prefetch_related('tag').all() 
        
    #     return context
    
    def get_context_data(self, **kwargs: reverse_lazy):
        context = super().get_context_data(**kwargs) 
        context['tags'] = Tags.objects.all()
        return context
    def get_queryset(self):
        return Tovar.objects.select_related('user').prefetch_related('tag').all() 

    



class TovarDetail(DetailView, FormView):
    model = Tovar
    form_class = ResponseForm
    template_name = 'AppBase/detail_tovar.html'
    


class CreateTovarCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('register:login')
    form_class = CreateTovarForm
    template_name = "AppBase/tovar_create.html"

    def form_valid(self, form):
        w = form.save(commit=False)
        w.user = self.request.user
        return super().form_valid(form)
    



    
class GetTags(ListView):
     template_name = 'AppBase/home.html'
     context_object_name = 'tovar'
     
     def get_queryset(self):
         return Tovar.objects.filter(tag = self.kwargs['pk'])
     