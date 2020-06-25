#!/usr/bin/env python3
from urllib import parse
from urllib import robotparser


class Robots():

    def __init__(self, domain):
        self.domain = domain


    def get_robots(self):
        URL_BASE = f'https://{self.domain}'
        parser = robotparser.RobotFileParser()
        parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
        parser.read()
        print(parser)

# test = Robots("partner.co.il")
# test.get_robots()