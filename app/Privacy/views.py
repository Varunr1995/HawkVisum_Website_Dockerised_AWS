from django.shortcuts import render

# Create your views here.


def privacypage(request):
    return render(request, 'privacy.html')
