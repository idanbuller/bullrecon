#!/usr/bin/env python3
from random import randint
import googlesearch
from tools import userage


class Git():

    def __init__(self, domain):
        self.domain = domain
        self.user_agent = userage.useragents()
        self.delay = randint(3, 8)
        self.search_max = 25
        self.file = f'github - {self.domain}.txt'


    def searcher(self):
        final = []
        query = f"inurl:github.com AND intext:{self.domain}"
        try:
            results = [url for url in googlesearch.search(
                query, num=self.search_max, start=0,
                stop=self.search_max, pause=self.delay, extra_params={"filter": "0"}, user_agent=self.user_agent)]
            final.extend(results)
            for file in final:
                print(file)
        except Exception as err:
            raise err
        # print(final)
        # with open(self.file, 'a') as f:
        #     print(f"[*] Creating {self.file} [*]")
        #     for i in final:
        #         if "pastebin.com" in i:
        #           f.write("%s\n" % i)
        #     f.close()



test = Git("partner.co.il")
test.searcher()