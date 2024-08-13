#this file is installed only in Pico W (controller)

from config import ssid,password
from picozero import LED
import network
import socket
import time
import machine

class controller:
    def __init__(self, ssid, password):
        #initilize pins for controller
        DEBUG_LED = LED(13)
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)
        max_wait = 10
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            DEBUG_LED.on()
            time.sleep(1)
            DEBUG_LED.off()

        if wlan.status() != 3:
            DEBUG_LED.on()
        else:
            status = wlan.ifconfig()
            print( 'ip = ' + status[0] )
            DEBUG_LED.off()
    
    def send_to_robot(self, action):
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            request = cl.recv(1024)
            print(request)
            cl.send(str(action))
            print("Sent:" + action)
            cl.close()

        except OSError as e:
            cl.close()
            print('connection closed')
            
    def read_inputs(self):
        pass
