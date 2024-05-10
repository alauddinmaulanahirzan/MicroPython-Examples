import ntptime
import time

class NTPSetup():
    def __init__(self):
        # Set Date Time
        ntptime.settime()

    # Get Date Time
    def getDateTime(self):
        self.devdatetime = time.localtime()
        self.devtime = str(self.devdatetime[3]+7)+":"+str(self.devdatetime[4])+":"+str(self.devdatetime[5])
        self.devdate = str(self.devdatetime[2])+"/"+str(self.devdatetime[1])+"/"+str(self.devdatetime[0])
        return self.devdate,self.devtime
    

def main():
    # Connect to Internet
    ntp = NTPSetup()
    devdate,devtime = ntp.getDateTime()
    print(devdate,devtime)
    
if __name__ == "__main__":
    main()