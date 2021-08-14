from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')

    # checkbox values check
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')

    # analyse the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""

    # checking if checbox is on"--punctuation"
    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove punctuation', 'analyze_text': analyzed}
        djtext = analyzed

    # checking if checbox is on"--capitalizing"
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Full Capitalized', 'analyze_text': analyzed}
        djtext = analyzed

        # checking if checbox is on"--new line remover"
    if newlinerem == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New line Removed', 'analyze_text': analyzed}
        djtext = analyzed

    #     checking is checkbox is on"----space remover--"
    if spaceremove == 'on':
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'Space Removing', 'analyze_text': analyzed}
        djtext = analyzed

    #     checking is checkbox is on"----extra  space remover--"
    if extraspaceremove == 'on':
        analyzed = ""
        for i, char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Removing', 'analyze_text': analyzed}
        djtext = analyzed


    #     checking is checkbox is on"----character count--"
    if charcount == "on":
        analyzed = 0
        for char in djtext:
            analyzed = analyzed + 1
        params = {'purpose': 'Character Count', 'analyze_text': analyzed}

    if removepunc != 'on' and fullcaps != 'on' and newlinerem != 'on' and spaceremove != 'on' and extraspaceremove != 'on' \
            and charcount != "on":
        return HttpResponse("ERROR ,PLEASE CLICK ON CHECK BOX")

    return render(request, 'analyze.html', params)
