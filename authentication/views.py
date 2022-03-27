from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, "authentication/index.html")	

def signup(request):
	return render(request, "authentication/singup.html")
	
def signin(request):
	return render(request, "authentication/singin.html")

def signout(request):
	return render(request, "index.html")


