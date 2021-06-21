import json

import requests


class Persistence:
    def __init__(self, url):
        self.url = url
        pass

    def getASDF(self, seed_id):
        results = requests.get(self.url + '/asdf')
        ret_val = json.loads(results.text)
        return ret_val
