import network
import mip

# Put Your SSID and Password
SSID: str = ""
Password: str = ""
reset = True # To Reset Network State and Force Connect

print(">> Start MicroPython Libs Installer ... ")
print(">> Connecting ... ")
wlan0 = network.WLAN(network.STA_IF)
if reset:
    wlan0.active(True)
        
    # Masukkan SSID dan Password
    wlan0.connect(SSID, Password)
    while not wlan0.isconnected():
        wlan0.active(True)
        pass
status = wlan0.isconnected()

if(status == True):
    print("==>> Connected")
    print(">> Verifying Libs urequests ...")
    try:
        import urequests
        print("==>> OK")
    except:
        print("==>> Failed. Installing Libs ... ")
        mip.install('urequests')
        
    print(">> Verifying Libs umqtt.robust ...")
    try:
        import umqtt.robust
        print("==>> OK")
    except:
        print("==>> Failed. Installing Libs ... ")
        mip.install("umqtt.robust")
        
    print(">> Verifying Libs umqtt.simple ...")
    try:
        import umqtt.simple
        print("==>> OK")
    except:
        print("==>> Failed. Installing Libs ... ")
        mip.install("umqtt.simple")
    print(">> Verifying Libs ssd1306 ...")
    try:
        import ssd1306
        print("==>> OK")
    except:
        print("==>> Failed. Installing Libs ... ")
        mip.install("ssd1306")
    print(">> Verifying Libs aioble ...")
    try:
        import aioble
        print("==>> OK")
    except:
        print("==>> Failed. Installing Libs ... ")
        mip.install("aioble")
    
else:
    print("==>> Connection Failed")
