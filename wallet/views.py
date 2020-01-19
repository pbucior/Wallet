from django.shortcuts import render
from .models import Operation

def home(request):
    context = {
        'operations': Operation.objects.all()
    }
    return render(request, 'home.html', context)