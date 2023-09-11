from api.requests.request import Request

class RegisterUserRequest(Request):

    def __init__(
        self,
        json: dict):

        super().__init__()
        self.json = json
        self.url = f'{self.url}/register'
        self.method = 'POST'
