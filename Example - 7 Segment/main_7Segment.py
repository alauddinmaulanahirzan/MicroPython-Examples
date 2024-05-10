from machine import Pin
from time import time,sleep
from utime import sleep_ms

# Map 1st Segment Pins
d1_p1 = Pin(2,Pin.OUT)		# E
d1_p2 = Pin(3,Pin.OUT)		# D
d1_p3 = Pin(4,Pin.OUT)		# DP
d1_p4 = Pin(5,Pin.OUT)		# C
d1_p5 = Pin(6,Pin.OUT)		# G
d1_p7 = Pin(22,Pin.OUT)		# B
d1_p10 = Pin(26,Pin.OUT)	# F
d1_p11 = Pin(27,Pin.OUT)	# A

# Map 1st Digit Pins
c1_1 = Pin(10,Pin.OUT)
c1_2 = Pin(9,Pin.OUT)
c1_3 = Pin(8,Pin.OUT)

# Map 2nd Segment Pins
d2_p1 = Pin(11,Pin.OUT)		# E
d2_p2 = Pin(12,Pin.OUT)		# D
d2_p3 = Pin(13,Pin.OUT)		# DP
d2_p4 = Pin(14,Pin.OUT)		# C
d2_p5 = Pin(15,Pin.OUT)		# G
d2_p7 = Pin(16,Pin.OUT)		# B
d2_p10 = Pin(17,Pin.OUT)	# F
d2_p11 = Pin(18,Pin.OUT)	# A

# Map 2nd Digit Pins
c2_1 = Pin(19,Pin.OUT)
c2_2 = Pin(20,Pin.OUT)
c2_3 = Pin(21,Pin.OUT)

# Store into Lists
c1_pins = [c1_1,c1_2,c1_3]
d1_pins = [d1_p11,d1_p7,d1_p4,d1_p2,d1_p1,d1_p10,d1_p5]
c2_pins = [c2_1,c2_2,c2_3]
d2_pins = [d2_p11,d2_p7,d2_p4,d2_p2,d2_p1,d2_p10,d2_p5]

# Define Numeric Patterns
num_patterns = [
        0b1111110,  # 0
        0b0110000,  # 1
        0b1101101,  # 2
        0b1111001,  # 3
        0b0110011,  # 4
        0b1011011,  # 5
        0b1011111,  # 6
        0b1110000,  # 7
        0b1111111,  # 8
        0b1111011   # 9
    ]

def turnDigits(board,power):
    if(board == 1):
        if(power):
            for control in c1_pins:
                control.value(0)
        else:
            for control in c1_pins:
                control.value(1)
    else:
        if(power):
            for control in c2_pins:
                control.value(0)
        else:
            for control in c2_pins:
                control.value(1)

def switchDigits(board,digit):
    if(board == 1):
        if(digit == 0):
            c1_pins[0].value(0)
            c1_pins[1].value(1)
            c1_pins[2].value(1)
        elif(digit == 1):
            c1_pins[0].value(1)
            c1_pins[1].value(0)
            c1_pins[2].value(1)
        else:
            c1_pins[0].value(1)
            c1_pins[1].value(1)
            c1_pins[2].value(0)
    else:
        if(digit == 0):
            c2_pins[0].value(0)
            c2_pins[1].value(1)
            c2_pins[2].value(1)
        elif(digit == 1):
            c2_pins[0].value(1)
            c2_pins[1].value(0)
            c2_pins[2].value(1)
        else:
            c2_pins[0].value(1)
            c2_pins[1].value(1)
            c2_pins[2].value(0)
            
def displayNumber(board,number):
    # Extract the individual digits from the number
    num1 = number // 100
    num2 = (number % 100) // 10
    num3 = number % 10

    # Turn Off All
    turnDigits(board,False)
    
    start_time = time()

    # Display the digits on the 7-segment display
    while time() - start_time < .25:
        switchDigits(board,0)
        setDisplay(board, 0, num3)
        sleep_ms(5)
        switchDigits(board,1)
        setDisplay(board, 1, num2)
        sleep_ms(5)
        switchDigits(board,2)
        setDisplay(board, 2, num1)
        sleep_ms(5)
    else:
        turnDigits(board,False)

def setDisplay(board,digit,num):    
    if(board == 1):
        # Set Pattern to Display
        for i, pin in enumerate(d1_pins):
            pattern = num_patterns[num]
            target = (pattern >> (6 - i)) & 1
            pin.value(target)
    else:
        # Set Pattern to Display
        for i, pin in enumerate(d2_pins):
            pattern = num_patterns[num]
            target = (pattern >> (6 - i)) & 1
            pin.value(target)

      
# Main Script
def main():
    board = 1
    powerOff = False

    if(powerOff):
        turnDigits(board,False)
    else:
        for data in range(100):
            displayNumber(board,data)

if __name__ == "__main__":
    main()