from django.contrib.auth.forms import UserCreationForm
from django.views import View

from django.shortcuts import render, redirect
from django.contrib.auth import login
from authorization.forms import UserLoginForm, UserRegistrationForm


class CustomAccountView(View):
    template_name = 'users/account.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'users/account.html')


class CustomLoginView(View):
    template_name = 'users/login.html'
    form = UserLoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('account')
        else:
            return render(request, self.template_name, {'form': form})


class CustomRegistrationView(View):
    form_class = UserCreationForm
    template_name = 'users/registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('login')
        return render(request, self.template_name, {'form': form})

# view через стандартную форму


# class UserRegistrationView(View):
#     template_name = 'users/registration.html'
#     form_class = UserRegistrationForm
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             new_user.set_password(form.cleaned_data['password'])
#             new_user.save()
#             login(request, new_user)
#             return redirect('login')
#         return render(request, self.template_name, {'form': form})
