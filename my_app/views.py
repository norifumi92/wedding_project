from django.shortcuts import render
from django.http import HttpResponse
#import redirect
from django.http import HttpResponseRedirect

#add entry form
from .forms import EntryForm

# index page
def index(request):
    #return HttpResponse('Hello, World!')
    return render(request, 'home.html')

# wedding page
def wedding(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = EntryForm(request.POST)
        
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    else:
        form = EntryForm()
        #return HttpResponse('Hello, World!')
        return render(request, 'wedding.html', {'form': form})
