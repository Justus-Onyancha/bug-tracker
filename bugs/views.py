from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def bugs(request):
    return render(request, 'bugs.html')

def bug(request, pk):
    return render(request, 'single-bug.html')