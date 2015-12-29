# In consumers.py
from channels import Group
from channels.decorators import channel_session

import json

# Connected to websocket.connect and websocjet.keepalive
@channel_session
def ws_add(message):
    query_params =  message.content['get']
    listen = query_params.get('listen')
    message.channel_session['listen'] = listen
    for i in listen:
        Group("listeners-"+str(i)).add(message.reply_channel)


# Connected to websocket.receive
@channel_session
def ws_message(message):
    #print message.content
    
    try:
        content = json.loads(message.content['content'])
        if 'uid' in content:
            Group("listeners-"+str(content['uid'])).send(message.content)       
    except:
        pass
    
    listen = message.channel_session.get('listen', [])
    for i in listen:
        Group("listeners-"+str(i)).add(message.reply_channel)
    
# Connected to websocket.disconnect
@channel_session
def ws_disconnect(message):
    listen = message.channel_session.get('listen', [])
    for i in message.channel_session['listen']:
        Group("listeners-"+i).discard(message.reply_channel)