from api.requests.request import Request

class GetResourceRequest(Request):
    
    def __init__(
        self, 
        resource_id: int):

        super().__init__()
        self.resource_id = resource_id
        self.url = f"{self.url}/unknown/{self.resource_id}"
        self.method = 'GET'