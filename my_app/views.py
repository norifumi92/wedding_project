from django.shortcuts import render
from django.http import HttpResponse
#import redirect
from django.http import HttpResponseRedirect

#add entry form
from .forms import AttendeeModelForm

#activate commit false
from django.forms import modelformset_factory

#import requests
import requests

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

            #Send message via Line Notify
            url = "https://notify-api.line.me/api/notify"
            token = "8F1U3P0vZH7iZ2pZosAiN9kyitXsxwMfXzUFXRdVqaw"

            first_name = form.data['first_name']
            last_name = form.data['last_name']
            message = first_name+" " + last_name + " just submitted the form now. "

            headers = {"Authorization" : "Bearer "+ token}
            
            payload = {"message" :  message}

            #send message
            requests.post(url ,headers = headers ,params=payload)

            # redirect to a new URL:
            return HttpResponseRedirect('/thanks')

    else:
        form = AttendeeModelForm()
        #set default value into the form attributes
        form.fields['event'].initial = 'wedding'

        #return HttpResponse('Hello, World!')
        return render(request, 'wedding.html', {'form': form})

def thanks(request):
    
    #render html
    return render(request, 'thanks.html')
