from hcsr04 import HCSR04
from time import sleep
from machine import Pin
from utime import sleep_ms

# Load Driver and Assign Each Pin
sensor = HCSR04(trigger_pin=4, echo_pin=5, echo_timeout_us=10000)
# LED Pin for Fun
led = Pin(2,Pin.OUT)
led.value(0)

# Create Blink Function
def blink():
    led.value(0)    
    sleep_ms(50)
    led.value(1)

# Main Script Here
while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    if(distance<=20): 
       blink()
    sleep(1)