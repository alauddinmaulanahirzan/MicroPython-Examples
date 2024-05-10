import serial
import time
import ast

ser = serial.Serial(
  port='/dev/ttyAMA0',
  baudrate = 115200,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

print("Receiving")

while True:
    data = (ser.readline())
    enc_data = data.decode("utf-8")
    if len(enc_data) != 0:
        data = "{"+enc_data+"}"
        data = ast.literal_eval(data)
        print(data)
