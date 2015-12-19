# In consumers.py
from channels import Group

# Connected to websocket.connect and websocjet.keepalive
def ws_add(message):
    print "1 ... add", message.reply_channel
    Group("chat").add(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    Group("chat").send(message.content)


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)