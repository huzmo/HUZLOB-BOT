import machine
from servo import Servo 
import time

class huzlobbot:
    def __init__(self):
        # initialize motors set all motors to initial position
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
        
        self.xAxis = machine.ADC(machine.Pin(27))
        self.yAxis = machine.ADC(machine.Pin(26))
        self.button = machine.Pin(16,machine.Pin.IN, machine.Pin.PULL_UP)
        
        self.first_servo_pos = 0   
        self.second_servo_pos = 0   
        self.third_servo_pos = 0     
        
        self.first_servo = Servo(pin_id=14)
        self.second_servo = Servo(pin_id=15)
        self.third_servo = Servo(pin_id=16)
        
        self.first_servo.write(self.first_servo_pos) 
        self.second_servo.write(self.second_servo_pos) 
        self.third_servo.write(self.third_servo_pos)
        
        self.forward_pin = machine.Pin(12, machine.Pin.OUT)
        self.backward_pin = machine.Pin(13, machine.Pin.OUT)
    def move_base_motor(self, a, b):
        
        self.forward_pin.value(a)
        self.backward_pin.value(b)
    
    def move_servo(self, servo_select):
        signal_pin = machine.Pin(21, machine.Pin.IN)
        signal_pin.value(1)
    
    def claw_control(self, state):
        signal_pin = machine.Pin(22, machine.Pin.OUT)
        signal_pin.value(state)
        
    def read_controller_input(self): #change to interupt handler if any issues in ghosting
        self.move_base_motor(0, 0)
        if self.sw7.value() == 0:
            print("base ccw")
            self.move_base_motor(1, 0)
        if self.sw8.value() == 0:
            print("base cw")
            self.move_base_motor(0, 1)
        if self.sw1.value() == 0:
            print("servo 1 up")
            self.first_servo_pos += 1
            self.first_servo.write(self.first_servo_pos)
        if self.sw4.value() == 0:
            print("servo 1 down")
            self.first_servo_pos -= 1
            self.first_servo.write(self.first_servo_pos)
        if self.sw2.value() == 0:
            print("servo 2 up")
            self.second_servo_pos += 1
            self.second_servo.write(self.second_servo_pos)
        if self.sw5.value() == 0:
            print("servo 2 down")
            self.second_servo_pos -= 1
            self.second_servo.write(self.second_servo_pos)
            pass
        if self.sw3.value() == 0:
            print("servo 3 up")
            self.third_servo_pos += 1
            self.third_servo.write(self.third_servo_pos)
        if self.sw6.value() == 0:
            print("servo 3 down")
            self.third_servo_pos -= 1
            self.third_servo.write(self.third_servo_pos)
        time.sleep(0.1)
    def read_joystick_input(self):
        xValue = self.xAxis.read_u16()
        yValue = self.yAxis.read_u16()
        buttonValue = self.button.value()
        self.move_base_motor(0, 0)
        self.claw_control(0)
        xStatus = "middle"
        yStatus = "middle"
        buttonStatus = "not pressed"
        
        if xValue <= 1000:
            xStatus = "left"
        elif xValue >= 60000:
            xStatus = "right"
        if yValue <= 600:
            yStatus = "down"
        elif yValue >= 60000:
            yStatus = "up"
        if buttonValue == 0:
            buttonStatus = "pressed"
            
        print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
        utime.sleep(0.1)
        
def main():
    my_bot = huzlobbot()
    while True:
        my_bot.read_controller_input()
        #my_bot.read_joystick_input()
        
        

if __name__ == "__main__":
    main()
        
        

