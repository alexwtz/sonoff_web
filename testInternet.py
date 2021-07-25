import requests

import time

import os

url = "http://www.kite.com"
timeout = 5
try:
  request = requests.get(url, timeout=timeout)
  print("Connected to the Internet")
except (requests.ConnectionError, requests.Timeout) as exception:
  print("No internet connection.")
  os.system('python off.py')
  time.sleep(5)
  os.system('python on.py')
