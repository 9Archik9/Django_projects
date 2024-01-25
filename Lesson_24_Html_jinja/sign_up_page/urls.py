from django.urls import path
from .views import SignUpPageView

app_name = 'sign_up_page'

url_patterns = [
    path('', SignUpPageView.as_view(), name='sign_up')
]
