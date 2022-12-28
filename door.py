import time
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #reed switch

# tact switch
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #A
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) #B
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) #C
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

#LED
#GPIO.setup(16, GPIO.OUT) 

while True:
    while True:
        if GPIO.wait_for_edge(17,GPIO.FALLING) != 0:
            GPIO.wait_for_edge(18,GPIO.RISING)
            print("OPEN!")
            if GPIO.wait_for_edge(22, GPIO.FALLING, timeout=60000, bouncetime=1000) != 0 :
                print("SAFE")
                break        
            else:
                print("OUT")
                import buzzer
                break

        elif GPIO.wait_for_edge(27,GPIO.FALLING) != 0:
            time.sleep(30)
            break
        else:
            print("wait now...")