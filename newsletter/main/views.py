from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse
from .utils import sendToSalesforce
import asyncio
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def sendToDatabase(request):
    data = json.loads(request.body)
    user = request.user
    email = data['visitor']['email'].lower()

    # Create an Email record 
    Email.objects.create(
        email = email,
    )
    sendEmail(request, email)
    print('Data:', request.body)
    asyncio.run(sendToSalesforce(email))
    return JsonResponse('Success',safe=False)

def sendEmail(request, email):
    subject = 'Thank you.'
    message = render_to_string('email/test_email.html')
    email = EmailMessage(subject, message, to=[email])

    if email.send():
        print("Success")
    else:
        print('Request:', request)