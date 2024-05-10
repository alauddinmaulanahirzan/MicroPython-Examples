from machine import Pin
from time import sleep
import dht
from utime import sleep_ms

# Define DHT Version (11 or 22) and Input Pin
sensor = dht.DHT22(Pin(16))
# Define Onboard LED Pin
led = Pin(2,Pin.OUT)
# Turn it off first
led.value(0)

# Define blink function
def blink():
    led.value(0)    
    sleep_ms(50)
    led.value(1)
    
# Main Script Here
while True:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    if(temp > 24.0 or hum > 49.0):
        blink()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    print("")
  except OSError as e:
    print('Failed to read sensor.')