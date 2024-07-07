from typing import Any
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm 
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.style = {
            'base': " bg-panel border-b-4 border-dark_panel",

        }
        
        self.fields['username'].widget.attrs.update({'class': f' row-start-2 col-start-1 {self.style.get("base")}',
                                                     'placeholder':'Имя',
                                                     'autocomplete':'off'})
        
        self.fields['password'].widget.attrs.update({'class': f' row-start-4 {self.style.get("base")} ',
                                                     'placeholder':'Пароль',
                                                     'autocomplete':'off'})

    class Meta:     
        model = get_user_model()
        fields = ('username', 'password')

        

class CreateUserForm(UserCreationForm):

    style = {
            'base': "h-[40px] transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50   w-full",

            }
    username = forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':' transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50  px-2 py-1 w-full','placeholder':"Имя пользователя"}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class':f' {style.get("base")} ','placeholder':"Пароль"}))
    password2 = forms.CharField(label='Повторите пароль',widget=forms.PasswordInput(attrs={'class':f'  {style.get("base")}','placeholder':"Повторите пароль"}))
        
    class Meta:
        model = get_user_model()
        fields = ['username','email','password1','password2']

        widgets = {'email':forms.EmailInput(attrs={
            'class':'  transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50  px-2 py-1 w-full row-start-3','placeholder':"Почта"
        })}

        order = ['username','email','password1','password2']