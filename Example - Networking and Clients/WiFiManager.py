import network
from urequests import get

class WiFiManager():
    def __init__(self,):
        self.reset = True

    # Koneksi Wi-Fi
    def connectWifi(self,SSID,Password):
        self.wlan0 = network.WLAN(network.STA_IF)
        if self.reset:
            self.wlan0.active(True)
            self.wlan0.connect(SSID, Password)
                
            while not self.wlan0.isconnected():
                self.wlan0.active(True)
                pass

        self.status = self.wlan0.isconnected()
        self.ip_addr = self.wlan0.ifconfig()
        return self.status,self.ip_addr
    
    # Tes Koneksi
    def testInternet(self):
        response = get("https://example.com/")
        status = response.status_code
        response.close()
        if status == 200:
            return True
        else:
            return False


def main():
    handler = WiFiManager()
    status,ip = handler.connectWLAN("","")
    print(ip,status)
    status = handler.testInternet()
    print(status)

if __name__ == '__main__':
    main()