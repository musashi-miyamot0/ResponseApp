from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView,DetailView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .forms import UserLoginForm, CreateUserForm,EditUserForm


# Create your views here.

class UserLogin(LoginView):
    next_page = reverse_lazy('home')
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = 'register/login.html'
    # def get_success_url(self) -> str:
    #     return reverse_lazy('home')
    
    

    
class CreateUser(CreateView):
    form_class = CreateUserForm
    template_name = 'register/register.html'
    
    def get_success_url(self) -> str:
        
        print(self.request.GET)

    


class Profile(LoginRequiredMixin,DetailView):
    template_name = 'register/profile.html'
    
    def get_object(self, queryset = None):
        return self.request.user
    

    
class EditProfile(UpdateView):
    template_name = 'register/editable_profile.html'
    form_class = EditUserForm
    
    def get_success_url(self) -> str:

        return redirect('register:view_profile')
    

    def get_object(self, queryset = None):
        return self.request.user
    
        
