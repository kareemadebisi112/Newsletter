from django.shortcuts import render
import json
from .models import *
from django.http import JsonResponse
from simple_salesforce import Salesforce, SFType, SalesforceLogin

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def sendToDatabase(request):
    data = json.loads(request.body)
    user = request.user
    email = data['visitor']['email']
    # Create a Visitor record 
    Visitor.objects.create(
        user = user,
        email = email
    )
    print('Data:', request.body)
    sendToSalesforce(user, email)
    return JsonResponse('Success',safe=False)

def sendToSalesforce(user, email):
    session_id, instance  = SalesforceLogin(username='kadebisi@kareemllc.com', password='luckykelsy3565!$', security_token='eh5e71IuPbNfXOYixtOD84yT6', client_id='My App')
    # sf = Salesforce(instance=instance, session_id=session_id)
    contact = SFType('Contact', session_id, instance)
    data = {
        'LastName': user.username,
        'Email':email,
        'From_Where__c': "Newsletter"
    }
    response = contact.create(data)
    if response['success'] == True:
        print("https://kareemllc2-dev-ed.develop.lightning.force.com/lightning/r/Contact/" + response['id']+'/view')
    return JsonResponse('Success',safe=False)

