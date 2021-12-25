import paho.mqtt.client as mqtt

from mqtt.models import CollarData

topics = [("collar/temperature", 1), ("collar/bellowing", 1),
          ("collar/accel/X", 1), ("collar/accel/Y", 1), ("collar/accel/Z", 1)]


def on_connect(client, userdata, flags, rc):
    client.subscribe(topics)


def on_message(client, userdata, msg):
    topic = msg.topic
    print(f"{topic}: {msg.payload}")
    collar_data = CollarData(topic=topic, message=msg.payload)
    collar_data.save()


client = mqtt.Client('raspy')
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
