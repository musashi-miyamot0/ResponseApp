from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'register'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='AppBase/home.html'), name='logout'),
    path('create_profile/', views.CreateUser.as_view(), name='create_profile'),

]
