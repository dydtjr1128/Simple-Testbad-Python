import paho.mqtt.client as mqtt
import time

# set broker ip address
ip = "192.168.0.53"
#ip = "192.168.0.23"
# set client number
num = 10
# client array
client = []

for i in range(0, num):
    client.append(mqtt.Client("Real"+str(i)))
    client[i].connect(ip)

print("All publishers connected. \n")

while(True):    
    #for i in range(1, 10):
      #  client[i].publish("EngineeringCenter/"+str(101+i)+"/fire","1" , qos = 0)
      #  client[i].publish("EngineeringCenter/"+str(101+i)+"/gas","1" , qos = 0)
      #  client[i].publish("EngineeringCenter/"+str(101+i)+"/humid","55" , qos = 0)
      #  client[i].publish("EngineeringCenter/"+str(101+i)+"/vibrate","1" , qos = 0)
      #  client[i].publish("EngineeringCenter/"+str(101+i)+"/temperature","24" , qos = 0)
    for i in range(2, 10):
        client[i].publish("TruthCenter/"+str(101+i)+"/fire","1" , qos = 0)
        client[i].publish("TruthCenter/"+str(101+i)+"/gas","1" , qos = 0)
        client[i].publish("TruthCenter/"+str(101+i)+"/humid","55" , qos = 0)
        client[i].publish("TruthCenter/"+str(101+i)+"/vibrate","1" , qos = 0)
        client[i].publish("TruthCenter/"+str(101+i)+"/temperature","24" , qos = 0)
# FutureCenter Code
# if you want to use this code, have to set num 29
#    for i in range(20, 29):
#        client[i].publish("FutureCenter/"+str(81+i)+"/fire","1" , qos = 0)
#        client[i].publish("FutureCenter/"+str(81+i)+"/gas","1" , qos = 0)
#        client[i].publish("FutureCenter/"+str(81+i)+"/humid","55" , qos = 0)
#        client[i].publish("FutureCenter/"+str(81+i)+"/vibrate","1" , qos = 0)
#        client[i].publish("FutureCenter/"+str(81+i)+"/temperature","24" , qos = 0)

    print("Fire Detection KITs message send. \n")
    time.sleep(1)



