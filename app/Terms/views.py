from django.shortcuts import render


# Create your views here.


def termspage(request):
    return render(request, 'terms.html')
