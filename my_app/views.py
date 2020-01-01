from django.shortcuts import render
from django.http import HttpResponse

# index page
def index(request):
    #return HttpResponse('Hello, World!')
    return render(request, 'home.html')

# wedding page
def wedding(request):
    #return HttpResponse('Hello, World!')
    return render(request, 'wedding.html')
