import time 
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ldr_pin = 3

def RCtime (RCpin):
 reading = 0
 GPIO.setup(RCpin, GPIO.OUT)
 GPIO.output(RCpin, GPIO.LOW)
 time.sleep(.1)
 
 GPIO.setup(RCpin, GPIO.IN)
 while (GPIO.input(RCpin) == GPIO.LOW):
  reading += 1
 return reading
 GPIO.cleanup()
while True: 
 LDRReading = RCtime(3)
 if 2000>LDRReading:
    
    Motor1E = 18
    Motor1A = 23
    Motor1B = 24
    print LDRReading
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT) 
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(2)

 if 4000<LDRReading<5500:
    
    Motor1E = 18
    Motor1A = 23
    print LDRReading
    GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.output(Motor1A,GPIO.LOW)
    
 if 5500<LDRReading<7000:
    
    Motor1E = 18
    Motor1A = 23
    Motor1B = 24
    print LDRReading
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT) 
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.LOW)
    sleep(2)
    GPIO.output(Motor1A,GPIO.LOW)
      
time.sleep(1)

