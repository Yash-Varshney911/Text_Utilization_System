from django.http import HttpResponse
from django.shortcuts import render
# I have created it.

def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the tEXT
    text = request.POST.get('text', 'default')
    # Check Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    nlr = request.POST.get('nlr', 'off') # For New Line Remover
    espr = request.POST.get('espr', 'off') # For Extra Space Remover
    charc = request.POST.get('charc', 'off') # For Character Counter
    # Checking which checkbox is on
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:""'\,<>./?@#$%^&*_~'''
        analyzed = " "
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
    #making a dictionary in python for showing our text at template.
        params = {'purpose' : "After Removing Punctuations", 'analyzed_text' : analyzed} # params = parameters
        text = analyzed


    if (fullcaps == "on"):
        analyzed = " "
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose' : "Changed to Uppercase", 'analyzed_text' : analyzed} # params = parameters
        text = analyzed


    if (nlr == "on"):
        analyzed = " "
        for char in text:
            if char != "\n" and char != "\r":    # \r = carriage return
                analyzed = analyzed + char
        params = {'purpose' : "New Line Removing", 'analyzed_text' : analyzed} # params = parameters
        text = analyzed


    if (espr == "on"):
        analyzed = " "
        for index, char in enumerate(text):
            if text[index] == ' ' and text[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose' : "After Removing Space", 'analyzed_text' : analyzed} # params = parameters
        text = analyzed


    if (charc == "on"):
        analyzed = " "
        for char in text:
            analyzed = len(text)
        params = {'purpose' : "Counted Character", 'analyzed_text' : analyzed} # params = parameters


    if(removepunc == "off" and fullcaps == "off" and nlr == "off" and espr == "off" and charc == "off"):
        return HttpResponse("<title>Error Page</title><body style ='background-color: #8540f5;'><div style ='color: red;height: 1000px;width: 100%; margin: 0px; font-size: 100px;font-weight: bolder;padding: 150px;box-sizing: border-box;'>Please, Select a check box</div></body>")

    return render(request, 'analyze.html', params)

