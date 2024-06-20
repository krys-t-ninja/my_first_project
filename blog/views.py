# Create your views here.
from django.shortcuts import HttpResponse, redirect 
from django.http import JsonResponse

def root_method(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"Placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog num {number}")

def delete(request, number):
    return redirect("/blogs")

def bonus(request):
    return JsonResponse({'title': 'my first blog', 'content': 'coding, yoga, meditation'})