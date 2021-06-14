from django.shortcuts import render

def hpme(request):
    return render(request, 'home.html')