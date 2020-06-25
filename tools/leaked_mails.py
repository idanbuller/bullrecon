#!/usr/bin/env python3
from random import randint
import googlesearch
from tools import userage


class Leaked():

    def __init__(self, domain):
        self.domain = domain
        self.user_agent = userage.useragents()
        self.delay = randint(3, 8)
        self.search_max = 25
        self.file = f'leaked_mails - {self.domain}.txt'


    def searcher(self):
        final = []
        query = f"inurl:mail-archive.com AND intext:partner.co.il"
        try:
            results = [url for url in googlesearch.search(
                query, num=self.search_max, start=0,
                stop=self.search_max, pause=self.delay, extra_params={"filter": "0"}, user_agent=self.user_agent)]
            final.extend(results)
        except Exception as err:
            raise err
        #print(final)
        # with open(self.file, 'a') as f:
        #     print(f"[*] Creating {self.file} [*]")
        #     for i in final:
        #         if "mail-archive.com" in i:
        #           f.write("%s\n" % i)
        #     f.close()
        for file in final:
            print(file)



#test = Leaked("partner.co.il")
#test.searcher()