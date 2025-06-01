import httpx

class SWCClient:

    def __init__(self, swc_base_url):
        self.swc_base_url = swc_base_url
    
    def get_health_check(self):
        # make the API call
        with httpx.Client(base_url=self.swc_base_url) as client:
            return client.get("/")
    