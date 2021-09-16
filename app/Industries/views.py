from django.shortcuts import render

# Create your views here.


def industriespage(request):
    return render(request, 'industries.html')


def educationpage(request):
    return render(request, 'education.html')


def automobilepage(request):
    return render(request, 'automobile.html')


def healthpage(request):
    return render(request, 'health.html')


def constructionpage(request):
    return render(request, 'construction.html')


def industrialpage(request):
    return render(request, 'industrial.html')


def gamingpage(request):
    return render(request, 'gaming.html')


def interiordesigningpage(request):
    return render(request, 'interiordesigning.html')
