from django.shortcuts import render
from django.http import HttpResponse
#import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

#add entry form
from .forms import AttendeeModelForm

#activate commit false
from django.forms import modelformset_factory

#import requests
import requests

#import generic functions
from my_app.functions import  notifyViaLine

# index page
def index(request):
    #return HttpResponse('Hello, World!')
    return render(request, 'home.html')

# wedding page
def wedding(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = AttendeeModelForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            #register data
            model = form.save(commit=False)
            model.save()
            #Get name
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            #Send message via Line Notify
            notifyViaLine(first_name, last_name)

            # redirect to a new URL:
            return HttpResponseRedirect('/thanks')
    else:
        form = AttendeeModelForm()
        #set default value into the form attributes
        form.fields['event'].initial = 'wedding'

        #return HttpResponse('Hello, World!')
        return render(request, 'wedding.html', {'form': form})

def thanks(request):
    #if referer is None, redirect to the home page.    
    referer = request.META.get('HTTP_REFERER')
    if referer is None:
            return HttpResponseRedirect('/')
    else:
        return render(request, 'thanks.html')

def reception(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = AttendeeModelForm(request.POST)

        # check whether it's valid:
        if form.is_valid():

            #register data
            model = form.save(commit=False)
            model.save()
            #Get name
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            #Send message via Line Notify
            notifyViaLine(first_name, last_name)
            
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks')

        else:
                return HttpResponseNotFound('<h1>Something was wrong. Contact Norifumi</h1>')  
    else:
        form = AttendeeModelForm()
        #set default value into the form attributes
        form.fields['event'].initial = 'reception'

        #return HttpResponse('Hello, World!')
        return render(request, 'reception.html', {'form': form})
