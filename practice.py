import utime #pico用time
from machine import Pin

Door = Pin(10, Pin.IN, Pin.PULL_UP) #reed switch

# tact switch
TactSwA = Pin(11, Pin.IN, Pin.PULL_UP) #A
TactSwB = Pin(12, Pin.IN, Pin.PULL_UP) #B
TactSwC = Pin(13, Pin.IN, Pin.PULL_UP) #C

Buzzer = Pin(14, machine.Pin.OUT) #buzzer

while True:
    while True:
        if TactSwA.value() == 0 :
            Buzzer.value(1)
            
        elif TactSwB.value() == 0 :
            Buzzer.value(0)
            
        else:
            print("off")