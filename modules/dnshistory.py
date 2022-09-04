from re import sub
import requests
from bs4 import BeautifulSoup

def getIps(domain):
    response = requests.get(f"https://dnshistory.org/historical-dns-records/a/{domain}")
    if (response.status_code == 200):
        soup = BeautifulSoup(response.content.decode(), "html.parser")
        ips = []
        try:
            for _a in soup.select("div#container > div#mainarea > div.clearfix > p > a"):
                ips.append(_a.text)
        except:
            pass
        return ips
    else:
        print("[ERR] DNSHistory Module failed.")
        return False