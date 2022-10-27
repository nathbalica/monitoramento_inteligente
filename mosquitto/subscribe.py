import random
import json
from paho.mqtt import client as mqtt_client
from postgres_connector.connect import Connect
from datetime import datetime
import pytz

broker = 'broker.hivemq.com' 
port = 1883 
topic = "/atmos-message" 
client_id = f'python-mqtt-{random.randint(0, 1000)}' 
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def convert_datetime(date_str):
    date_convert = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    date_convert = date_convert.replace(tzinfo=pytz.UTC).astimezone(pytz.timezone("EST"))
    date_convert = date_convert.strftime("%Y-%m-%d %H:%M:%S.%f %z")
    return date_convert

def insert_db(payload):
    query = (f"""insert into measurer_data(mac_name, date_measurer, rssi, va, vb, vc, ia, ib, ic, wa, wb, wc) 
        values ('{payload['mac']}', '{convert_datetime(payload['date'])}', 
        {payload['rssi']}, {payload['va']}, {payload['vb']}, {payload['vc']},
        {payload['ia']}, {payload['ib']}, {payload['ic']},
        {payload['wa']}, {payload['wb']}, {payload['wc']})""")
             
    cnx = Connect("postgres_atmos", "atmos_db", "atmos", "atmos", 5432)
    print("Inserting data...")
    cnx.insert_row(query)

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        payload = json.loads(msg.payload.decode())
        print(payload)
        insert_db(payload)
        
    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()