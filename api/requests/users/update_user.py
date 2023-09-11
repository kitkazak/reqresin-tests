from api.requests.request import Request

class UpdateUserRequest(Request):
    
    def __init__(
        self, 
        user_id: int,
        json: dict):

        super().__init__()
        self.user_id = user_id
        self.json = json
        self.url = f"{self.url}/users/{self.user_id}"
        self.method = 'PUT'