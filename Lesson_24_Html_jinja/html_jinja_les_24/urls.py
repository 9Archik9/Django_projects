"""
URL configuration for html_jinja_les_24 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from home_page.urls import urlpatterns as home_page
from sign_up_page.urls import url_patterns as sign_up_page
from sign_in_page.urls import url_patterns as sign_in_page
from success_sign_in_page.urls import url_patterns as success_sign_in_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_page)),
    path('sign-up/', include((sign_up_page, 'sign_up_page'), namespace='sign_up_page')),
    path('sign-in/', include(sign_in_page),
    path('success/', include((success_sign_in_page, 'success_sign_in_page'), namespace='success_sign_in_page')))
]
