from django.shortcuts import render

# Create your views here.


def faqpage(request):
    return render(request, 'faq.html')
