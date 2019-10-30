import requests
import json

def randomizer():
  return requests.get("http://jservice.io/api/random").json()
  

       
    