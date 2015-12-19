# In routing.py
channel_routing = {
    "websocket.connect": "sensors.consumers.ws_add",
    "websocket.keepalive": "sensors.consumers.ws_add",
    "websocket.receive": "sensors.consumers.ws_message",
    "websocket.disconnect": "sensors.consumers.ws_disconnect",
}