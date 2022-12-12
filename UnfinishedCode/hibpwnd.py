import json
import requests
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv()


hibp_api_key = os.getenv("hibp_api_key")
url = "https://haveibeenpwned.com/api/v3/breachedaccount/basti@exotix.eu"
payload={}
headers = {
  'hibp-api-key': str(hibp_api_key),
  'format': 'application/json',
  'timeout': '2.5',
  'HIBP': str(hibp_api_key),
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)