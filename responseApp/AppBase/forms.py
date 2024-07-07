from .models import Response,Tovar
from django import forms

class ResponseForm(forms.ModelForm):
    class Meta:
        base_class = 'input_base'
        model = Response
        labels = {field.name: '' for field in model._meta.fields}
        fields = ('title', 'text',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': f'{base_class} title_input',
                'placeholder': 'Тема'
            }),
            'text': forms.TextInput(attrs={
                'class': f"{base_class} description_input",
                'placeholder': 'Содержимое'
            }),
            'tovar_rel': forms.TextInput(attrs={}),
        }

class CreateTovarForm(forms.ModelForm):
    
    class Meta:
        base_class = '"h-[40px] transition-colors focus:border-dark_panel border-0 focus:border-b-4 focus:outline-none focus:ring-0 bg-panel border-b-4 border-dark_panel/50'
        model = Tovar
        fields = ("title","image",'description')
        
        widgets = {
            'title': forms.TextInput(attrs={
               'class': base_class,"placeholder":'Название'
            }),"image":forms.FileInput(attrs={
                'class': f"{base_class}" ,
            }),
            'description': forms.Textarea(attrs={
                "class":"flex-1 rounded-2xl transition-colors focus:!border-opac border-0 focus:border-b-0 focus:outline-none focus:ring-0 bg-panel border-b-0 border-dark_panel/50",'rows':32, 'cols':171
            })
            
        }

