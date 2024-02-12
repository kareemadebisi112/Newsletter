from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse
from .utils import sendToSalesforce
import asyncio
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from .forms import SubscriberForm

# Create your views here.
class Email():
    emails = []

    def addEmail(self, name):
        self.emails.append(name)
    def clearEMail(self):
        self.emails = []

emailClass = Email

def index(request):
    return render(request, 'main/index.html')

def sendToDatabase(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        # form = SubscriberForm(request.POST)
        print('Form:',form['email'][0])
        # if form.is_valid():
        #     subscriber = form.save()
        #     context = {'email': subscriber.email}
        #     print(context)
        # else:
        #     print('Not valid')
















    # data = json.loads(request.body)
    # user = request.user
    # email = data['visitor']['email'].lower()

    # Add Email to Collection
    # emailClass.addEmail(emailClass, email)
    # TODO: Add Email Verification
    # sendEmail(request, email, context)
    # print(emailClass.emails)

    # Create an Email record 
    # Email.objects.create(
    #     email = email,
    # )

    # print('Data:', request.body)
    # asyncio.run(sendToSalesforce(email))
    return JsonResponse('Success',safe=False)

def sendEmail(request, email, context):
    subject = 'Thank you.'
    message = render_to_string('email/test_email.html', context)
    email = EmailMessage(subject, message, to=[email])

    if email.send():
        print("Success")
    else:
        print('Request:', request)