from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
class UserLoginForm(AuthenticationForm):

    class Meta:

        base:str = " bg-panel border-b-4 border-dark_panel",


        model = get_user_model()
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': f" row-start-2 col-start-1 {base}",
                'placeholder':'Имя',
                'autocomplete':'off'}),
            'password': forms.PasswordInput(attrs={
                'class': f" row-start-4  {base}",
                'placeholder':'Пароль',
                'autocomplete':'off'}),
            
        }
    

        

class CreateUserForm(UserCreationForm):

    style = {
            'base': "h-[40px] transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50   w-full",

            }
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':' transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50  px-2 py-1 w-full','placeholder':"Имя пользователя"}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':f' {style.get("base")} ','placeholder':"Пароль"}))
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput(attrs={'class':f'  {style.get("base")}','placeholder':"Повторите пароль"}))
        
    class Meta:
        model = get_user_model()
        fields = ['username','email','photo','password1','password2']

        widgets = {'email':forms.EmailInput(attrs={
            'class':'  transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50  px-2 py-1 w-full row-start-3','placeholder':"Почта"
        })}

        order = ['username','email','password1','password2']
        
class EditUserForm(forms.ModelForm):
    
    class Meta:
        
        base= "h-[40px] transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50   w-full",

            
        model = get_user_model()
        fields = ['username','photo','first_name','last_name']
        
        widgets = {
            'username':forms.TextInput(attrs={'class':f' col-start-2 row-start-2 {base}','placeholder':"Имя пользователя"}),
            'first_name':forms.TextInput(attrs={'class':f'col-start-2 row-start-4 {base}','placeholder':"Имя"}),
            'last_name':forms.TextInput(attrs={'class':f' col-start-2 row-start-6 {base}','placeholder':"Фамилия"}),
            'photo':forms.FileInput(attrs={'class':f' hidden','placeholder':"Фото"}),
            
        }