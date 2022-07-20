from django.shortcuts import render

def home(request):
    name = 'Bo'
    return render(request, 'route/home.html', {'name':name})
