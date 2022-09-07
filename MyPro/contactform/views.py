from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . import forms
from django.core.mail import send_mail


# Create your views here.
def index (request):
    form = forms.contact_form ()
    if request.method == 'POST':
        form = forms.contact_form (request.POST)
        html = 'we have received your mail'
        if form.is_valid ():
            html = html + " : Your e-mail is sent."
    else:
        html = 'Sending mail for first time'

    # send_mail (
    #     subject = subject,
    #     message = message,
    #     from_email = settings.EMAIL_HOST_USER,
    #     recipient_list = [settings.RECIPIENT_ADDRESS]
    # )
    return render (request,'index1.html',{'html': html,'form': form})
