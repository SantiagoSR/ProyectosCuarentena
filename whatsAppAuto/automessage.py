from twilio.rest import Client 
 
account_sid = 'ACCOUNT_SID' 
auth_token = 'AUTH_TOKEN' 
client = Client(account_sid, auth_token) 
def send_mms():

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hola este es un saludo corto xd',      
                              to='whatsapp: +NUMBER' 
                          ) 
 
    print(message.sid)
