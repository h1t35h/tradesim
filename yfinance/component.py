from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json

headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate, sdch, br',
           'Accept-Language': 'en-GB,en-US;q=0.8,en;q=0.6',
           'Connection': 'keep-alive',
           'Host': 'www.nseindia.com',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
           'X-Requested-With': 'XMLHttpRequest'}


BASE_LINK = "https://www.nseindia.com/api/equity-stockIndices?index=__INDEX__"

"""
Returns list of 
"""
def get_index_components(index, verbose=False):
  call_url = BASE_LINK.replace("__INDEX__", index)
  

  if verbose:
    print(f"Calling for url: {call_url}")

  data = None
  count = 0
  while data is None and count < 5:
    try: 
      response  = requests.get(call_url, headers=headers)
      data = json.loads(response.text)
    except:
      count+=1
      pass
  print(data["data"])
  return data


get_index_components("NIFTY 50")
