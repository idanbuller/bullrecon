#!/usr/bin/env python3
from whois import whois


class whois_query():

    def __init__(self, domain):
        self.domain = domain

    def whoisSearch(self):
        try:
            query = whois(self.domain)
            print("Domain: ", query.domain)
            print("Update time: ", query.get('updated_date'))
            print("Expiration time: ", query.get('expiration_date'))
            print("Name server: ", query.get('name_servers'))
            print("Email: ", query.get('emails'))
            raporIcerik = ""
            raporIcerik += "Domain: " + query.domain + "\n"
            raporIcerik += "Update time: " + str(query.get('updated_date')) + "\n"
            raporIcerik += "Expiration time: " + str(query.get('expiration_date')) + "\n"
            raporIcerik += "Name server: " + str(query.get('name_servers')) + "\n"
            raporIcerik += "Email: " + str(query.get('emails')) + "\n"
        except Exception as err:
            raise err

# test = whois_query("tau.ac.il")
# test.whoisSearch()