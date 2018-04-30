from django.shortcuts import render

# Create your views here.

def phones_home(request):
    return render(request, 'twophones/phones_home.html', {})