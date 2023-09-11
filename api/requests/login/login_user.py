from api.requests.request import Request

class LoginUserRequest(Request):
    
    def __init__(
        self, 
        json: dict):

        super().__init__()
        self.json = json
        self.url = f"{self.url}/login"
        self.method = 'POST'
