import paho.mqtt.client as mqtt



def mqttService(message):
    broker_address= "<broker ip >" #address of broker
    client = mqtt.Client("P1") #create new instance
    client.connect(broker_address) #connect to broker
    client.publish(message)