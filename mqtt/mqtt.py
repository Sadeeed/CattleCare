import paho.mqtt.client as mqtt

from mqtt.models import CollarData

topics = [("collar/temperature", 1), ("collar/bellowing", 1),
          ("collar/accel/X", 1), ("collar/accel/Y", 1), ("collar/accel/Z", 1), ("collar/bpm", 1)]


def on_connect(client, userdata, flags, rc):
    client.subscribe(topics)


def on_message(client, userdata, msg):
    topic = msg.topic
    message = msg.payload.decode("utf-8")
    print(f"{topic}: {message}")
    collar_data = CollarData(topic=topic, message=message)
    collar_data.save()


client = mqtt.Client('raspy')
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
