from django.urls import path
from authorization.views import CustomLoginView, CustomAccountView, CustomRegistrationView


urlpatterns = [
    path('login', CustomLoginView.as_view(), name='login'),
    path('account', CustomAccountView.as_view(), name='account'),
    path('register', CustomRegistrationView.as_view(), name='register'),
]
