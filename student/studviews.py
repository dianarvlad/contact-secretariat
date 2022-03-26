from django.shortcuts import render
from django.http import HttpResponse

def login_stud(request):
     return render(request, 'student/login_stud.html')
