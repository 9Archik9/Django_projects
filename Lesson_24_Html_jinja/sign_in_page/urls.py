from sign_in_page.views import SignInPageView
from django.urls import path

app_name = 'sign_in_page'

url_patterns = [
    path('', SignInPageView.as_view(), name='sign-in_page'),
]
