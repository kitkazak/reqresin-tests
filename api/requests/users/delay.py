from api.requests.request import Request

class DelayRequest(Request):
    
    def __init__(
        self, 
        delay: int):

        super().__init__()
        self.delay = delay
        self.url = f"{self.url}/users"
        self.method = 'GET'
        self.parameters = {
            'delay': self.delay,
        }
