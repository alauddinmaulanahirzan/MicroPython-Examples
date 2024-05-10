from machine import UART
from machine import Pin
import utime as time
from dht import DHT11

# LED
led = Pin(25, Pin.OUT)

# Relay
# relay = Pin(27, Pin.OUT)

# UART
uart = UART(0,baudrate = 115200)

# Sensor
pin = Pin(28, Pin.IN)
sensor = DHT11(pin)

led.off()

print("=> Starting Temp and Humid Monitor")

while True:
    time.sleep(1)
    led.on()
    t = (sensor.temperature())
    h = (sensor.humidity())
    sensor.measure()
    print("==> Temperature: {}".format(t))
    print("==> Humidity: {}".format(h))
    print()
    message = "'temp':{},'hum':{}".format(t,h)
    uart.write(message.encode('utf-8'))
    time.sleep(1)
    led.off()