from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    captcha=CaptchaField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username' : forms.TextInput(),
            'email' : forms.EmailInput(),
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput()}

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class Login(AuthenticationForm):
    captcha=CaptchaField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "password", 'captcha')
        widgets = {
            'username' : forms.TextInput(),
            'email' : forms.EmailInput(),
        }