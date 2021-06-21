import json

import requests


class Waveform:
    def __init__(self, url):
        self.url = url
        pass

    def save(self):
        results = requests.post(self.url)
        ret_val = json.loads(results.text)
        return ret_val
