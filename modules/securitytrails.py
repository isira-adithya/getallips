import requests
import json

def getIps(domain, apikey):
    url = f"https://api.securitytrails.com/v1/history/{domain}/dns/a"

    headers = {
        "Accept": "application/json",
        "APIKEY": apikey
    }

    response = requests.get(url, headers=headers)
    pagesCount = json.loads(response.text)['pages']
    records = json.loads(response.text)['records']
    if (pagesCount != 1):
        for i in range(pagesCount):
            # Repeat the same action if there is more pages
            _ = i + 2
            if (_ >= pagesCount):
                break
            url = f"https://api.securitytrails.com/v1/history/{domain}/dns/a?page={_}"
            response = requests.get(url, headers=headers)
            for record in json.loads(response.text)['records']:
                records.append(record)
    _ips = []
    for record in records:
        for obj in record['values']:
            _ips.append(obj['ip'])
    return _ips
    