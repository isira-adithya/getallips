## Setup
Before running the script, install BeautifulSoup and Requests python modules by running the following
```
pip install beautifulsoup4
pip install requests
```

## Security Trails API
If you want to use SecurityTrails API, Create an environmental variable called `GI_STAPIKEY` and add your SecurityTrails API key inside that variable.

## Output
Every Unique IP address detected will be written to `./allips.txt`