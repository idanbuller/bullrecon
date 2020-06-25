#!/usr/bin/env python3
import builtwith

class Webalayzer():

    def __init__(self, domain):
        self.domain = domain
        self.url = f"http://{domain}"

    def web(self):
        try:
            website = builtwith.parse(self.url)
            for key, value in website.items():
                print(key + ":", ", ".join(value))

        except Exception as err:
            print(err)

# test = Webalayzer("partner.co.il")
# test.web()