import utime #pico用time
from machine import Pin

Door = Pin(10, Pin.IN, Pin.PULL_UP) #reed switch

###青20　黄色19　赤18

# tact switch
TactSwA = Pin(11, Pin.IN, Pin.PULL_UP) #A
TactSwB = Pin(12, Pin.IN, Pin.PULL_UP) #B
TactSwC = Pin(13, Pin.IN, Pin.PULL_UP) #C

Buzzer = Pin(14, Pin.OUT) #buzzer
Led = Pin(18, Pin.OUT)
Yel = Pin(19, Pin.OUT)
Blu = Pin(20, Pin.OUT)

while True:
    while True:
        if TactSwA.value() == 0 :
            Led.value(1)
            while True :
                if Door.value() == 0:  
                    Yel.value(1)
                    utime.sleep(10)
                    if  TactSwC.value() == 0:
                        Blu.value(1)
                        utime.sleep(5)
                        break        
                    else:
                        Buzzer.value(1)
                        utime.sleep(2)
                        break
        elif TactSwB.value() == 0:
            Yel.value(1)
            utime.sleep(30)
            break
        else:
            Led.value(0)
            Yel.value(0)
            Blu.value(0)
            Buzzer.value(0)
            break