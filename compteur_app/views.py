from django.shortcuts import render, redirect
from .models import Counter

def counter_view(request):
    # Retrieve or create the counter
    counter, created = Counter.objects.get_or_create(id=1)
    return render(request, 'counter.html', {'counter': counter})

def increment(request):
    counter, created = Counter.objects.get_or_create(id=1)
    counter.value += 1
    counter.save()
    return redirect('/')

def decrement(request):
    counter, created = Counter.objects.get_or_create(id=1)
    counter.value -= 1
    counter.save()
    return redirect('/')

