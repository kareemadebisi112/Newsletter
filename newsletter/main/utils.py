from simple_salesforce import Salesforce, SalesforceLogin

# 
class SalesforceHelper:
    session_id = ''
    instance = ''
    def setup():
        session_id, instance  = SalesforceLogin(username='kadebisi@kareemllc.com', password='luckykelsy3565!$', security_token='eh5e71IuPbNfXOYixtOD84yT6', client_id='My App')

async def sendToSalesforce(email):
    session_id, instance  = SalesforceLogin(username='kadebisi@kareemllc.com', password='luckykelsy3565!$', security_token='eh5e71IuPbNfXOYixtOD84yT6', client_id='My App')
    sf = Salesforce(instance=instance, session_id=session_id)
    data = [{
        'Name': email,
    }]
    response = sf.bulk.Email__c.insert(data)
    print(response)
    for item in response:
        if item['success'] == True:
            print("https://kareemllc2-dev-ed.develop.lightning.force.com/lightning/r/Email/" + item['id']+'/view')
