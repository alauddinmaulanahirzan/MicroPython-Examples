from urequests import get

## Blynk API Class
class BlynkAPI:
    # Initialize Blynk API Class
    def __init__(self):
        self.server_address: str = "blynk.cloud"
        self.token: str = "<Put Yout Token Here>"
        self.fetch_link = f"https://{self.server_address}/external/api/get?token={self.token}&"
        self.update_link = f"https://{self.server_address}/external/api/update?token={self.token}&"

    # Method to get vpin value (pin: v0, v1, v2, ...)
    def fetchPin(self, pin: str):
        response = get(self.fetch_link+pin)
        result = response.json() # For some reason this line will cause some devices to stuck. Only to limited to Blynk API Response
        status = response.status_code
        response.close()
        return status, result # Return Status Code and Result

    # Method to update vpin value (pin: v0, v1, v2, ...; value: int or str)
    def updatePin(self, pin: str, value):
        if type(value) is int:
            value = str(value)
        response = get(self.update_link+pin+"="+value)
        status = response.status_code
        response.close
        return status # Return Status Code
    

## Usage Sample
def main():
    # Connect to Network
    # Initialize Class
    api = BlynkAPI()
    status, result = fetchPin("v0") # Fetch vPin v0
    status = updatePin("v1", 10) # Update vPin v1 to 10 