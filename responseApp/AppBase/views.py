from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView, FormView, CreateView

from .models import Tovar
from .forms import ResponseForm, CreateTovarForm 
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(ListView):
    model = Tovar
    template_name = 'AppBase/home.html'
    paginate_by = 10
    context_object_name = 'tovar'
    
    

def allresponse(request):
    return render(request, 'AppBase/home.html')

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
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permission_denied_message'] = self.permission_denied_message
        return context