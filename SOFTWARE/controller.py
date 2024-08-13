#this file is installed only in Pico W (controller)

from config import ssid,password
from picozero import LED
import network
import socket
import time
import machine

class controller:
    def __init__(self, ssid, password):
        
        self.sw1 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
        self.sw2 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
        self.sw3 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)
        self.sw4 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
        self.sw5 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
        self.sw6 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)
        self.sw7 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
        self.sw8 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
        self.switch_list = [self.sw1,self.sw2,self.sw3,
                            self.sw4,self.sw5,self.sw6,
                            self.sw7,self.sw8,]
        DEBUG_LED = LED(16)
        self.STATE_LED = LED(15)
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(ssid, password)
        
        max_wait = 10
        
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            DEBUG_LED.blink()
            time.sleep(1)

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
            
    def read_controller_input(self): #change to interupt handler if any issues in ghosting
        if self.sw7.value() == 0:
            print("base ccw")
            self.STATE_LED.on()
            
        if self.sw8.value() == 0:
            print("base cw")
            self.STATE_LED.on()
            
        if self.sw1.value() == 0:
            print("servo 1 up")
            self.STATE_LED.on()
            
        if self.sw4.value() == 0:
            print("servo 1 down")
            self.STATE_LED.on()
            
        if self.sw2.value() == 0:
            print("servo 2 up")
            self.STATE_LED.on()
            
        if self.sw5.value() == 0:
            print("servo 2 down")
            self.STATE_LED.on()
            
        if self.sw3.value() == 0:
            print("servo 3 up")
            self.STATE_LED.on()
            
        if self.sw6.value() == 0:
            print("servo 3 down")
            self.STATE_LED.on()
            
        time.sleep(0.1)
        self.STATE_LED.off()
    
def main():
    my_controller = controller(ssid, password)
    while True:
        my_controller.read_controller_input()

          

if __name__ == "__main__":
    main()
