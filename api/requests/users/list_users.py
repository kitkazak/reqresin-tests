from api.requests.request import Request

class ListUsersRequest(Request):
    
    def __init__(
        self, 
        page_id: int, 
        per_page_id: int):

        super().__init__()
        self.page_id = page_id
        self.per_page_id = per_page_id
        self.url = f"{self.url}/users"
        self.method = 'GET'
        self.parameters = {
            'page_id': self.page_id,
            'per_page_id': self.per_page_id
        }
