from binascii import unhexlify
from paho.mqtt import client as mqtt_client
import message 
import paho.mqtt.subscribe as substribe

broker = ''
port = 1883
topic = ""
client_id = f''
username = ''
password = ''
c_bytes = 0

#####################################################################
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
#####################################################################

def _counterBytes_(data):
    result = len(data)
    return result

#######################################################################
def subscribe(client: mqtt_client):
    def on_message(client, usaerdata, msg):
        global c_bytes
        _FromMqtt_ = msg.payload[2:-1]
        _unserialize_ = unhexlify(_FromMqtt_)
        _protobuf_ = message.payload()
        _sparkplug_ = _protobuf_.FromString(_unserialize_)
        print(_sparkplug_)
        print("Bytes:", c_bytes)


    client.subscribe(topic)
    client.on_message = on_message
