from django.shortcuts import render

def home(request):
    return render(request, 'thing/home.html', {})
