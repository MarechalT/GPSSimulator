import paho.mqtt.client as mqtt
import time
import random
import config

client = mqtt.Client()
client.connect(config.mqtt_server_ip, config.mqtt_server_port, config.mqtt_server_keepalive)

latitude = config.position[0]
longitude = config.position[1]
altitude = config.position[2]

while True:
    randomval = random.uniform(config.range[0], config.range[1])
    randomval2 = random.uniform(config.range[0], config.range[1])

    latitude += randomval
    longitude += randomval2

    timestamp = int(time.time())
    simu = '{{"name":{0},"lat":{1}, "lon":{2}, "alt":{3}, "ts":{4}}}'.format(config.name, latitude, longitude, altitude, timestamp)
    print(simu)
    client.publish("tracker", simu)
    time.sleep(2)
client.disconnect()