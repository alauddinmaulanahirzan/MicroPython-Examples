from machine import Pin, SoftI2C
# This Driver Lib may not installed yet
import ssd1306

# Define i2c peripheral
i2c = SoftI2C(sda=Pin(5), scl=Pin(4))
# Configure I2C Display Resolution
display = ssd1306.SSD1306_I2C(128, 64, i2c)
# Test Output
display.text('Hello, World!', 0, 0, 1)
display.show()