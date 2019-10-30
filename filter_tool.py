import requests
import json
import copy
import datetime


def search(inputs):
  loop_counter = 0 
  returnlist = []
  len_returnlist = 0
  offset = 0 


  json_url = "http://jservice.io/api/clues?"

  if inputs["difficulty"] != "":
    json_url = json_url+ "value="+inputs['difficulty']+"&"



  if inputs['category_ID']:
    json_url = json_url+ "category=" + inputs["category_ID"] + "&"


  if inputs["date"] and inputs["date2"]:
    json_url = json_url + "min_date=" + str(inputs["date"])+ "&max_date=" + str(inputs["date2"])+"&"



  json_url_og = json_url
  json_data = requests.get(json_url_og).json()



  while json_data != [] and len_returnlist <= int(inputs["show_count"]):
    if offset > 2000:
      return returnlist   #cut off search if time takes too long 

      
    for dictionary in json_data:
      if inputs['searchword'] in dictionary["answer"].split() or inputs['searchword'] in dictionary["question"].split() or inputs['searchword'] in dictionary["category"]["title"].split():
        returnlist.append(dictionary)
        len_returnlist += 1

    offset += 100
    json_url = json_url_og + "offset=" + str(offset)
    json_data = requests.get(json_url).json()



  return returnlist
  



  
  




    


   