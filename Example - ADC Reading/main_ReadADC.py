from machine import ADC
import time

# Assign ADC Pin 0 to Sensor
sensor = ADC(0)

# Repeatedly Read u16 value and print
while True:
    result = sensor.read_u16()
    print(result)
    time.sleep(1)