import requests, json;

class Temperature:

    temperature_now = 0

    def __init__(self):
        self.temperature_now

    def get_Datas(self):
        request = requests.get('https://api.hgbrasil.com/weather?woeid=456385');
        new_datas = json.loads(request.content);
        self.temperature_now = new_datas['results']['temp'];
        return self.temperature_now;