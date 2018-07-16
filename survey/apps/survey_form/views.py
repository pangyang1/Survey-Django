from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render (request, 'surveyform/index.html')

def formProcess(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Locations": request.POST['dojoLocations'],
        "Favorite Langauge": request.POST['favLang'],
        "Comments": request.POST['comments']
    }
    return redirect('/showResults')

def showResults(request):
    print "Go to Show Results"
    print request.session
    return render(request, 'survey_form/results.html')
# Create your views here.
