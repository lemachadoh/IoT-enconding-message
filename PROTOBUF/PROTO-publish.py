from binascii import hexlify
from paho.mqtt import client as mqtt_client
import message 
import time
import PROTO_msg_pb2  as MENSAGEM

##########################################################################
#conectar mqtt
broker = ''
port = 1883
topic = ""
client_id = f''
username = ''
password = ''

def connect_mqtt():
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
###########################################################################

def publish(client):
    while True:
        msg_count = message.payload()
        msg_publish = hexlify(msg_count.SerializeToString())
        time.sleep(1)
        msg = f"{(msg_publish)}"
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")




def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

