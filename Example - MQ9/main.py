from machine import ADC, Pin
from mq9 import MQ
import time

# Global Params
gas = ADC(Pin(34))
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
        result = round(read_mq9(mq)[2],3)
        
        if result < 0:
            result = 0
        elif result > 1000:
            result = 1000
        
        print(f"Carbon Monoxide : {result} ppm")
    
if __name__ == "__main__":
    main()