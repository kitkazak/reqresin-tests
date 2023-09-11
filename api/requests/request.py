import requests

class Request():

    def __init__(self):
        # BASE URL
        self.url = 'https://reqres.in/api'
        self.method = ''
        self.parameters = {}
        self.json = {}
        self.response = {}

    def send(self):

        if len(self.parameters) != 0:
            self.url = self.url + '?'
            for key, value in self.parameters.items():
                if value != None:
                    self.url = f'{self.url}{key}={value}&'
            self.url = self.url[:-1]
                
        match self.method:
            case 'GET':
                if len(self.json) == 0:
                    self.response = requests.get(self.url)
                else:
                    self.response = requests.get(
                        self.url,
                        json=self.json)
            case 'POST':
                if len(self.json) == 0:
                    self.response = requests.post(self.url)
                else:
                    self.response = requests.post(
                        self.url,
                        json=self.json)
            case 'DELETE':
                if len(self.json) == 0:
                    self.response = requests.delete(self.url)
                else:
                    self.response = requests.delete(
                        self.url,
                        json=self.json)
            case _:
                raise BaseException('No method provided')