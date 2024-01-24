from sign_in_page.views import SignInPageView
from django.urls import path

urlpatterns = [
    path('', SignInPageView.as_view(), name='sign-in_page')
]
