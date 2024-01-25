from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm


class SignUpPageView(View):

    template_name = 'signup_page.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_up_page:sign_up')
        return render(request, self.template_name, {'form': form})
