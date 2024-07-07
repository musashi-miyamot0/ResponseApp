from django.shortcuts import render 
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from .forms import UserLoginForm, CreateUserForm

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

    


