from machine import ADC, Pin
from mq9 import MQ
import time
import dht
import network
import ntptime
import urequests

# Global Params
gas = ADC(Pin(35))
led = Pin(2,Pin.OUT)
led.value(0)

# Function to read MQ9 Sensor
def read_mq9(mq):
    while True:
        try:
            adc = gas.read_u16()
            sensor_volt = gas.read_uv()/1000000
            perc = mq.MQPercentage()
            break
        except:
            pass
    co = perc["CO"]*1000
    
    if co >= 10000:
        cp = 10000
    
    result = [adc,sensor_volt,co]
    return result

# Function to Blink
def blink():
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
    
# Function to Blink Faster
def blink_fast():
    led.value(1)
    time.sleep(0.25)
    led.value(0)
    time.sleep(0.25)

# Main Script
def main():    
    # Calibrate Sensor
    print("Calibrating MQ-9 Sensor")
    led.value(1)
    while True:
        try:
            mq = MQ()
            break
        except:
            pass
    led.value(0)
    print("Calibrated")
    print("")
    
    print("Start Monitoring:")
    print("")
    
    while True:
        result = read_mq9(mq)
        print(f"ADC Value : {result[0]}, Sensor Voltage : {result[1]} Volt, and Carbon Monoxide : {result[2]} ppm")
    
if __name__ == "__main__":
    main()