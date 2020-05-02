import paho.mqtt.client as mqtt
import time
import random
import config

client = mqtt.Client()
client.connect(config.mqtt_server_ip, config.mqtt_server_port, config.mqtt_server_keepalive)

while True:
    randomval = random.uniform(config.range[0], config.range[1])
    randomval2 = random.uniform(config.range[0], config.range[1])

    latitude = config.position[0] + randomval
    longitude = config.position[1] + randomval2
    altitude = config.position[2]
    timestamp = int(time.time())
    simu = '{{"name":{0},"lat":{1}, "lon":{2}, "alt":{3}, "ts":{4}}}'.format(config.name, latitude, longitude, altitude, timestamp)
    print(simu)
    client.publish("tracker", simu)
    time.sleep(5)
client.disconnect()