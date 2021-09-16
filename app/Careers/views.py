from django.shortcuts import render
# from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def careerspage(request):
    if request.method == 'POST':
        Name = request.POST['Applicant_Name']
        Email = request.POST['Applicant_Email']
        Subject = request.POST['Applicant_Subject']
        Message = request.POST['Applicant_Message']
        Resume = request.POST['Applicant_Resume']

        send_mail(Subject,
                  f"From{Name},({Email}) {Message} {Resume}",
                  settings.EMAIL_HOST_USER,
                  [settings.EMAIL_HOST_USER],
                  fail_silently=False,
                  )
        return render(request, 'careers.html')

    else:
        return render(request, 'careers.html')
