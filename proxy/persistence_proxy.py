import json
import time
import requests


class Persistence:
    def __init__(self, url):
        self.url = url
        pass

    def getASDF(self, seed_id):
        start = time.perf_counter()
        results = requests.get(self.url + '/itaca/asdf')
        ret_val = json.loads(results.text)
        end = time.perf_counter()
        print('time elapsed', f'{end - start:0.4f} s')
        return ret_val
