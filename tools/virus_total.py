#!/usr/bin/env python3
import requests


class VirusTotal():

    def __init__(self, domain):
        self.domain = domain
        self.url = 'https://www.virustotal.com/vtapi/v2/domain/report'
        self.params = {'apikey': 'f15e85a43385bfb4d81b640d8f069e127184815ee31a79863548aee72aa76945', 'domain': self.domain}
        self.reuslt = []
        self.file = f'virus_total - {self.domain}.txt'

# 6ed05894f8e3bc4a38da5a71709fd1708b5b1172 - neriya
# f15e85a43385bfb4d81b640d8f069e127184815ee31a79863548aee72aa76945 - idan

    def fileSearch(self):
        # print(f"Searching for malicious files communicating with {self.domain}.\n")
        response = requests.get(self.url, params=self.params)
        parsed_response = response.json()
        try:
            for i in parsed_response['detected_downloaded_samples']:
                tmp = (i['sha256'], f"  {i['positives']}/{i['total']}")
                self.reuslt.append(tmp)
        except BaseException:
            pass
        try:
            for i in parsed_response['detected_referrer_samples']:
                tmp = (i['sha256'], f"  {i['positives']}/{i['total']}")
                self.reuslt.append(tmp)
        except BaseException:
            pass
        try:
            for i in parsed_response['detected_communicating_samples']:
                tmp = (i['sha256'], f"  {i['positives']}/{i['total']}")
                self.reuslt.append(tmp)
        except:
            pass

        # if len(self.reuslt) == 0:
        #     print("No related malicious files found.")
        # else:
        #     print(f"Found {len(self.reuslt)} related malicious files! \n")
        print(self.reuslt)
        for file in self.reuslt:
            print(file)

# test = VirusTotal("tau.ac.il")
# test.fileSearch()