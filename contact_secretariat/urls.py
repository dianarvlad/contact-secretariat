"""contact_secretariat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from secretariat import secretarviews
from student import studviews

class MyLogoutView(LogoutView):
    template_name = 'index.html'

urlpatterns = [
    path('admin/', admin.site.urls),
	# path('', views.start1),
	path('student/', studviews.login_stud),
	path('secretariat/',secretarviews.login ),
    path('home/', include('authentication.urls')),
	path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('signout/', MyLogoutView.as_view()),
]
