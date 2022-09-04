# Importing modules
import modules.rapiddns
import modules.securitytrails
import modules.dnshistory
import sys
import os

ips = []
gi_stapikey = ""

# Checking if the subdomain is specified or not
if (len(sys.argv) == 2):
    if (sys.argv[1].count(".") == 1):
        domain = sys.argv[1]
        pass
    else:
        print("[ERR] Please specify a valid domain, not a subdomain.")
        exit()
else:
    print("[ERR] Please specifiy the domain.\n      Ex: `python3 main.py example.com`")
    exit()

# Checking if security trails api key is specified or not
if (os.environ.get('GI_STAPIKEY')):
    gi_stapikey = os.environ.get('GI_STAPIKEY')
else:
    print("[WARN] SecurityTrails API key not found.")


# Getting IPs from RapidDNS
try:
    ips.extend(modules.rapiddns.getIps(domain=domain))
except Exception as err:
    print("[ERR] Something went wrong with the RapidDNS api.")
    print(err)

# Getting IPs from SecurityTrails
if (gi_stapikey != ""):
    try:
        ips.extend(modules.securitytrails.getIps(domain=domain, apikey=gi_stapikey))
    except Exception as err:
        print("[ERR] Something went wrong with the SecurityTrails api. (Probably API credit limit is exceeded)")
        print(err)
# Getting IPs from dnshistory.org
try:
    ips.extend(modules.dnshistory.getIps(domain=domain))
except Exception as err:
    print("[ERR] Something went wrong with the dnshistory.org api.")
    print(err)

# Removing Duplicates from the ips
ips = list(set(ips))

# Writing data to allips.txt
with open('allips.txt', 'w') as _wF:
    for ip in ips:
        _wF.write(ip + "\n")
    _wF.close()
    print(f"[SUCCESS] Found {len(ips)} IP addresses")