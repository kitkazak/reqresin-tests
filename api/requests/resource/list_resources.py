from api.requests.request import Request

class ListResourcesRequest(Request):

    def __init__(self):

        super().__init__()
        self.url = f'{self.url}/unknown'
        self.method = 'GET'
