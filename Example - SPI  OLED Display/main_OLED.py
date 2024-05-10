from machine import Pin, SoftSPI
import ssd1306

sck = Pin(14)		# D0
scl = Pin(13)		# D1

spi = SoftSPI(baudrate=500000, polarity=1, phase=0, sck=sck, mosi=scl, miso=Pin(12))

rst = Pin(4)	# reset
dc = Pin(5)		# data/command
cs = Pin(15)	# chip select, some modules do not have a pin for this

display = ssd1306.SSD1306_SPI(128, 64, spi, dc, rst, cs)

# display.text('Hello, World!', 0, 0, 1)
# display.show()

display.fill(0)
display.fill_rect(0, 0, 32, 32, 1)
display.fill_rect(2, 2, 28, 28, 0)
display.vline(9, 8, 22, 1)
display.vline(16, 2, 22, 1)
display.vline(23, 8, 22, 1)
display.fill_rect(26, 24, 2, 4, 1)
display.text('MicroPython', 40, 0, 1)
display.text('SSD1306', 40, 12, 1)
display.text('OLED 128x64', 40, 24, 1)
display.show()