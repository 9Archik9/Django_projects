from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['repeat_password']


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def get_user(self):
        return self.instance

    def authenticate_user(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        return user


