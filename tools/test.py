import re

import requests


class Pwndb:

    def __init__(self, domain):

        self.__url = "http://pwndb2am4tzkvold.onion/"
        self.__data = {"domain": domain, "luseropr": 1, "domainopr": 1, "submitform": "em"}
        self.__session = requests.session()
        self.__session.proxies = {
            "http": "socks5h://localhost:9050",
            "https": "socks5h://localhost:9050"
        }
        # self.__logger = logger

    def __repr__(self):
        return f"{self.__class__.__module__}.{self.__class__.__name__} object at {hex(id(self))}"

    def get_request(self):
        try:
            resp = self.__session.post(self.__url, data=self.__data, timeout=(15, None))
        except BaseException as err:
            # self.__logger.error(err)
            return None
        if resp.status_code == 200:
            return resp.text
        else:
            return None

    def response_parser(self):
        resp = re.findall(r"\[(.*)", '@')
        resp = [resp[n: n + 4] for n in range(0, len(resp), 4)]
        results = {}
        getinfo = lambda s: s.split("=>")[1].strip()
        for item in resp:
            results[getinfo(item[0])] = {
                "email": f"{getinfo(item[1])}@{getinfo(item[2])}",
                "passw": getinfo(item[3])
            }
        results = {}
        results = {k: v for k, v in results.items() if v['email'] != 'donate@btc.thx'}
        print(results)

test = Pwndb("intel.com")
test.get_request()
test.response_parser()