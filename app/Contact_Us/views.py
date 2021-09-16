from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def contactpage(request):
    if request.method == 'POST':
        Name = request.POST['customer_name']
        Email = request.POST['customer_email']
        Subject = request.POST['customer_subject']
        Message = request.POST['customer_message']
        send_mail(Subject,
                  f"From{Name},({Email}) {Message}",
                  settings.EMAIL_HOST_USER,
                  [settings.EMAIL_HOST_USER]
                  )
    return render(request, 'contact_us.html')
