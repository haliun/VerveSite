from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages, auth
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives,BadHeaderError
from django.shortcuts import render_to_response,render,redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.utils.translation import ugettext as _
from .forms import ContactForm
def home(request):
    return render(request, 'index.html')
@csrf_exempt
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('name', '')
            from_email = request.POST.get('email', '')
            company = request.POST.get('company', '')
            telephone=request.POST.get('telephone','')
            message = request.POST.get('message', '')
            body = 'Email: ' + from_email +''+ ', ' +'Company: '+company+''+ ',  ' + 'Message: ' + message + ''+'.  '+'Tel: '+telephone+''+'.'
            to_email = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, body, from_email, ['amour_haliuka@yahoo.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, "index.html", {'form': form})