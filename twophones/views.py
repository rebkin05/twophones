from django.shortcuts import render
from django.utils import timezone
from .models import ThingEntry

def phones_home(request):
    twothings = ThingEntry.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'twophones/phones_home.html', {'twothings': twothings})


