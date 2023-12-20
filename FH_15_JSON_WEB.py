# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:15:18 2020

@author: Hrishikesh Pisal
"""

# Encoding and Decoding Simple Data Types
# import urllib
from urllib import request
import json
 # This module provides functions for encoding binary data to 
 # printable ASCII characters
import base64

def getJSONdata(myurl):
    import urllib
    import pprint as pp
    # myurl = urllib.request.quote(myurl)
    response = urllib.request.urlopen(myurl)
    data = response.read().decode("utf-8")
    print(type(data))
    pp.pprint(data,indent=5)
    
def  get_country_info(decoded_json):
    # print(type(decoded_json))
    # print(decoded_json["countries"][0])
    # print(type(decoded_json["countries"][0]))
    # print(decoded_json["countries"][0]['country'])
    # print(decoded_json["countries"][0]['country'].keys())
    # print(decoded_json["countries"][0]['country'].values())
    c_code = input('Please enter the country code : ')
    c_code = c_code.upper()
    for country in decoded_json["countries"]:
        # print(list(country['country'].values())[0])
        if list(country['country'].values())[0] == c_code:
            print(f'Code : {c_code}, Name : {list(country["country"].values())[1]}')
            break
    else:
        print(f"Country with code {c_code} does not exist")

def download_counrty_data(url):
    import urllib
    import pprint as pp
    response = urllib.request.urlopen(url)
    json_data = response.read()
  
     # Deserialize s (a str, bytes or bytearray instance containing a JSON document)
     # to a Python object.
    decoded = json.loads(json_data)
    # pp.pprint(decoded)     
    indent_data(decoded)
    # get_country_info(decoded)
    
def indent_data(decoded):
    # print('DATA:', repr(decoded))
    # returns JSON formatted string
    print( json.dumps(decoded, sort_keys=True, indent=5))
   
def image_demo(image_file_name, json_file_name):
   
    with open(image_file_name,"rb") as img_file:
        imagedata = img_file.read()
    # print(imagedata)
    data = {}
    
    # Encode the bytes-like object imagedata, 
    # which can contain arbitrary binary data, 
    # and return bytes containing the base64-encoded data
    encoded_byte_data = base64.encodebytes(imagedata)
    
    # Decode the contents of the binary input file
    data['img'] = encoded_byte_data.decode('utf-8') 
   
      
    #Alternatively : just one line
    # data['img'] = base64.encodebytes(imagedata).decode('utf-8')
    # print( data['img'])
    
    import datetime
    author_dict = {
        "native":"রবীন্দ্রনাথ ঠাকুর",
        "name" : "Robindronath Tagore",
        "born" : datetime.date(1861, 5, 7).__str__(),
        "children" :  5,
        "photo" : data
        }
    
    # Serialize object author_dict as a JSON string
    json_str = json.dumps(author_dict)
    
    # write the resulting binary data to the output file. 
    # input and output must be file objects.
    output_file = open(json_file_name,"w")
    output_file.write(json_str)
    output_file.close()        

def parseJSON(json_file, image_file):
    file_object = open(json_file,"r")
    json_data = file_object.read()
     # Deserialize s (a str, bytes or bytearray instance containing a JSON document)
     # to a Python object.
    decoded = json.loads(json_data)
    print("Name of author : ",decoded["name"])
    print("Name Native : ",decoded["native"])
    print("Number of children : ",decoded["children"])
    print("Born : ",decoded["born"])
    
    img_data = decoded["photo"]
    # print(img_data['img'])
    encode_img = img_data['img'].encode("utf-8")
    # Decode the bytes-like object s, 
    # which must contain one or more lines of base64 encoded data, 
    # and return the decoded bytes.
    decode_img_data = base64.decodebytes(encode_img)
    img_file_object = open(image_file,'wb')
    img_file_object.write(decode_img_data)
    img_file_object.close()
    file_object.close()

if __name__ == '__main__':
    # url = "https://api.nasa.gov/planetary/apod?api_key=mccLeBfvFkCCKS7CCDyIoxgykVruzZey8rhIZmMu"
    # url = "https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=mccLeBfvFkCCKS7CCDyIoxgykVruzZey8rhIZmMu"
    # url = "http://vocab.nic.in/rest.php/orgn/intr/im/json"
    # url = "http://vocab.nic.in/cla.php?cat=sg&state=tn&info=orgn&district=TN002&format=json"
    # getJSONdata(url)
    
    # country_info_url ="http://vocab.nic.in/rest.php/country/json"

    # download_counrty_data(country_info_url)
  
    
    # Indian Mission data
    # http://vocab.nic.in/rest.php/orgn/intr/im/json
    
    image_file_name = "tagore.jpg" #birthday.jpg" # tagore.jpg
    json_file_name = "author.txt"
    # image_demo(image_file_name,json_file_name)
    parseJSON(json_file_name,"thakur.jpg")
    
    
