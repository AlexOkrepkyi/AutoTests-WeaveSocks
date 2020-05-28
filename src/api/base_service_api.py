import os


class BaseServiceApi:

    def __init__(self):
        self._base_url = os.environ["BASE_URL"]
        self._headers = {"content-type": "application/json"}
