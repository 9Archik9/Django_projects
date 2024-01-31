from django.urls import path

from home_page.views import HomePageView


urlpatterns = [
    path('home-page/', HomePageView.as_view(), name='home')
]
