from django.shortcuts import render
from django.views import View

from home_page.models import News


class HomePageView(View):
    news = News.objects.all().order_by('-date')

    def get(self, request):
        return render(request, 'home_page.html', context={'news': self.news})
