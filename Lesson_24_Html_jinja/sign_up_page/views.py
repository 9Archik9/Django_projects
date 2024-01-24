from django.shortcuts import render
from django.views import View


class SignUpPageView(View):
    def get(self, request):
        return render(request, 'signup_page.html')
