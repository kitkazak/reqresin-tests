from api.requests.request import Request

class DeleteUserRequest(Request):
    
    def __init__(
        self, 
        user_id: int):

        super().__init__()
        self.user_id = user_id
        self.url = f"{self.url}/users/{self.user_id}"
        self.method = 'DELETE'