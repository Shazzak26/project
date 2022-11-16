from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def about(request):
    context = {'data': "hellow this is about page."}
    return render(request, 'about.html')

def medicine(request):
    return render(request, 'medicine.html')