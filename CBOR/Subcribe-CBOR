from paho.mqtt import client as mqtt_client
from interpretador import  _toJson_, _deserializar_
import paho.mqtt.subscribe as substribe

broker = ''
port = 1883
topic = ""
client_id = f''
username = ''
password = ''
c_bytes = 0

##############################################################################################
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

################################################################################################

def _counterBytes_(data):
    result = len(data)
    return result

##########################################################################################
def subscribe(client: mqtt_client):
    def on_message(client, usaerdata, msg):
        global c_bytes
        _FromMqtt_ = msg.payload[2:-1]
        _unserialize_ = _deserializar_(_FromMqtt_)
        _sparkplug_ = _toJson_(_unserialize_)
        c_bytes += _counterBytes_(_FromMqtt_)
            
        print("Bytes:", c_bytes)
        print(_sparkplug_)
        
    client.subscribe(topic)
    client.on_message = on_message

def run():   
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    



if __name__ == '__main__':
    run()
    

