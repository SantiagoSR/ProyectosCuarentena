from twilio.rest import Client 
 
account_sid = 'ACbd52b1ffc3bd84b178f6822583f04795' 
auth_token = '7a117da18d4a9527bbff4ebcfbc4b87c' 
client = Client(account_sid, auth_token) 
def send_mms():

    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hola este es un saludo corto xd',      
                              to='whatsapp:+573108329407' 
                          ) 
 
    print(message.sid)
