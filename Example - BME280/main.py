from machine import Pin, SoftI2C
from time import sleep
import BME280

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)

while True:
    bme = BME280.BME280(i2c=i2c)
    temperature = bme.temperature
    humidity = bme.humidity
    pressure = bme.pressure

    print('Temperature is: ', temperature)
    print('Humidity is: ', humidity)
    print('Pressure is: ', pressure)
    sleep(10)