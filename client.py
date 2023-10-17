import os

import requests


class Client:
    API_ADDRESS = os.getenv("API_ADDRESS")
    HEADERS = {
        "X-Forwarded-Host": os.getenv("X_FORWARDED_HOST"),
        "Host": os.getenv("HOST"),
    }

    def __init__(self, path, params: dict = None, headers: dict = None):
        self.path = path
        self.params = params
        self.headers = headers
        if self.headers:
            self.HEADERS.update(self.headers)

    # def _get_full_address(self):
    #     return self.API_ADDRESS + self.path[1:] if self.path.startswith("/") else
    #
    #
    # def post(self, data):
    #     pass
