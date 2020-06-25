#!/usr/bin/env python3
from tools import iswho, pastebin, linkedin, webyzer, robots, leaked_mails, virus_total


class Bull():

    def __init__(self, domain):
        self.domain = domain


    def is_who(self):
        iswho.whois_query(self.domain).whoisSearch()

    def webyzer(self):
        webyzer.Webalayzer(self.domain).web()

    def robots(self):
        robots.Robots(self.domain).get_robots()

    def leaked_mails(self):
        leaked_mails.Leaked(self.domain).searcher()

    def virus_total(self):
        virus_total.VirusTotal(self.domain).fileSearch()

    def pastebin(self):
        pastebin.Pastes(self.domain).searcher()

    def linkedin(self):
        linkedin.Linkedin(self.domain).search()




test = Bull(str(input("Enter STRING / DOMAIN NAME: ")))
print("Who is it?\n==================================")
test.is_who()
print("\nWeb Technologis\n==================================")
test.webyzer()
print("\nRobots.txt\n==================================")
test.robots()
print("\nLeaked Mails\n==================================")
test.robots()
print("\nMalicious Files\n==================================")
test.virus_total()
print("\nPastebin\n==================================")
test.pastebin()
print("\nLinkedin\n==================================")
test.linkedin()
