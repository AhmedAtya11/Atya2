from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'pages/index.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    return render(request, 'pages/login.html')