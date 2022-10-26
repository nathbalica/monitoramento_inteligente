import paho.mqtt.client as mqtt_client
import random
import time

broker = 'broker.hivemq.com' 
port = 1883 
topic = "/atmos-message" 
client_id = f'python-mqtt-{random.randint(0, 1000)}' 
# username = 'emqx' 
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def create_message():
    return {
                "mac": "DE:DD:26:74:3D:70", 
                "date": '2022-10-19T00:00:00.000z',
                "rssi":-60,
                "va": 223,
                "vb": 222,
                "vc": 231,
                "ia": 10,
                "ib": 4,
                "ic": 2,
                "wa": 840,
                "wb": 960,
                "wc": 1200,
    }
def publish(client):
     while True:
         time.sleep(1)
         msg = f"messages: {create_message()}"
         result = client.publish(topic, msg)
         # result: [0, 1]
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
