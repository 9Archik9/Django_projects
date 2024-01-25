from django.urls import path
from .views import SuccessView

app_name = 'success_sign_in_page'

url_patterns = [
    path('success/', SuccessView.as_view(), name='success'),
]
