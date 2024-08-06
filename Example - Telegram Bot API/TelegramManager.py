import requests

class TelegramManager:
    def __init__(self):
        self.token = ""
        self.chat_id = ""
        self.url_text = "https://api.telegram.org/bot{}/sendMessage?chat_id={}".format(self.token,self.chat_id)

    def sendMessage(self,text):
        url = self.url_text+"&text={}".format(text)
        response = requests.get(url)
        response.close()

def main():
    tg = TelegramManager()
    tg.sendMessage("Test")

if __name__ == '__main__':
    main()