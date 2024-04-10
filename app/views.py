from django.shortcuts import render

from .models import Counter

def home(request):
    counter = Counter.objects.last()
    if not counter:
        counter = Counter.objects.create()
    
    counter.count += 1
    counter.save()
    counter = {
        "count": counter.count,
    }
    return render(request, "app/home.html", counter)