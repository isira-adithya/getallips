import requests
from bs4 import BeautifulSoup

def getIps(domain):
    response = requests.get(f"https://rapiddns.io/subdomain/{domain}?full=1")
    if (response.status_code == 200):
        soup = BeautifulSoup(response.content.decode(), "html.parser")
        ips = []
        try:
            for _a in soup.select("div.progress-table-wrap > table > tbody > tr > td > a"):
                ips.append(_a.text)
        except:
            pass
        return ips
    else:
        print("[ERR] RapidDNS Module failed.")
        return False