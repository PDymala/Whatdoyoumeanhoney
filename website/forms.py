from django import forms
from django.forms import ModelForm
from .models import Meme

class MemeForm(ModelForm):
    class Meta:
        model = Meme
        # fields = "__all__"
        fields = ('title', 'prompt')
        # labels = {
        #     'title' : '',
        #     'prompt' : '',

        # }
        widgets = {

            # 'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'title'}), uzywamy CRISPY nie trzbe formatowac
            # 'prompt' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'prompt'}),
            
            'title' : forms.TextInput(),
            'prompt' : forms.TextInput(),

        }