from django.shortcuts import render
from django.views import View


class SuccessView(View):
    template_name = 'success_signin_page.html'

    def get(self, request):
        return render(request, self.template_name)
