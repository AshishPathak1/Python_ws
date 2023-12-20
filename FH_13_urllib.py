# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:04:27 2019

@author: Hrishikesh Pisal
"""

## Module urllib.urlrequest contains a function called 
## urlopen that opens a web page for reading. 
## urlopen returns a file-like object that you can use 
## much as if you were reading a local file.
        
import urllib.request
import urllib.parse
import io

def encode_url_demo():
    query = 'Hellö+Wörld @ Python🐍'
    # The quote() function by default uses UTF-8 encoding scheme.
    encoded_str = urllib.parse.quote(query)
    print("Encoded String :",encoded_str)
    # Hell%C3%B6%2BW%C3%B6rld%20%40%20Python%F0%9F%90%8D
    
    # The quote() function encodes space characters to %20. 
    # If you want to encode space characters to plus sign (+), 
    encoded_str = urllib.parse.quote_plus(query)
    print("Encoded String :",encoded_str)
    # Hell%C3%B6%2BW%C3%B6rld+%40+Python%F0%9F%90%8D
    query = 'Hello जय कुमार'
    encoded_str = urllib.parse.quote_plus(query)
    print("Encoded String :",encoded_str)
     # Hello+%E0%A4%9C%E0%A4%AF++%E0%A4%95%E0%A5%81%E0%A4%AE%E0%A4%BE%E0%A4%B0
    query  = 'https://hi.wikipedia.org/wiki/२९_जनवरी'
    encoded_str = urllib.parse.quote_plus(query)
    print("Encoded String :",encoded_str)

# Using urllib.urlopen() will return a response object,
# which can be handled similar to a file.

# Pass the URL to urlopen() to get a “file-like” handle to the remote data.
def requestDemo(url):
    from urllib import request
    
    # url = urllib.parse.urlencode(url)
    # on success return http.client.HTTPResponse
    
    response = request.urlopen(url)
    # Class whose instances are returned upon successful connection. 
    print(type(response))
    print('RESPONSE:', response)
    print('URL     :', response.geturl())
    # print("Encoding :",response.encoding)
    headers = response.info()
    print('DATE    :', headers['date'])
    print('HEADERS :')
    print('---------')
    print(headers)
    
    data = response.read().decode('utf-8')
    print('LENGTH  :', len(data))
    print('DATA    :')
    print('---------')
    print(data)
    
    
def readWebPage(url):
    from urllib import request
# The file-like object returned by urlopen() is iterable:
    with request.urlopen(url) as reponse:
        print(reponse)
        for line in reponse:
            line = line.strip()
            # print(type(line))
            line = line.decode('utf-8')
            print(line)

# def saveWebPage(urlToRead, destFile):
#     from urllib import request
#     outFile = open(destFile, mode="wt")
#     with request.urlopen(urlToRead) as response:
#         for line in response:
#             # line = line.strip()
#             # print("Original : ",type(line))
#             line = line.decode('utf-8')
#             # print(line)
#             # print("After decoding : ", type(line))
#             outFile.write(line)
#             outFile.write("</br>")
        
#     # page = request.urlopen(url).read() #->byte String
#     # page = 
#     # outFile.write(page)
#     outFile.close()


def saveWebPage(urlToRead, destFile):
    from urllib import request
    outFile = open(destFile, mode="wt")
    response =  request.urlopen(urlToRead) 
    for line in response:
        # line = line.strip()
        # print("Original : ",type(line))
        line = line.decode('utf-8')
        # print(line)
        # print("After decoding : ", type(line))
        outFile.write(line)
        # outFile.write("</br>")
        
    # page = request.urlopen(url).read() #->byte String
    # page = 
    # outFile.write(page)
    outFile.close()
    
def passingParameters():
    # query_parms = {'username':'hrishipisal@gmail.com', 'password':'acd1234'}
    # encoded_parms=urllib.parse.urlencode(query_parms).encode('utf-8')
    # response = urllib.request.urlopen("https://stackoverflow.com/users/login", encoded_parms)
    
    url = "https://www.bing.com/search?"
    query_parms = {'query':'q=pune'}
    encoded_parms=urllib.parse.urlencode(query_parms).encode('utf-8')
    # url = url+encoded_parms.decode('utf-8')
    # print(url)
    url = url+encoded_parms
    print(url)
    response = urllib.request.urlopen(url)
    print("Response Code :",response.code)
    data = response.read()
    print(data)
    outFile = open("d:\\sai.html","w")
    outFile.write(str(data))
    outFile.close()
    # text = io.TextIOWrapper(response)
    # print("***************************")
    # print(text.read())
    # print(data,file=open("d:/account.html","w"))



# The urllib.parse module provides functions for manipulating URLs and their component parts, to either break them down or build them up.
from urllib.parse import urlparse 

# Parsing
# The return value from the urlparse() function is a 
# ParseResult object that acts like a tuple with six elements.
def url_parse_demo(url):
    # url = 'http://netloc/path;param?query=arg#frag'
    # url = 'https://www.bing.com/search?q=pune'
    parsed = urlparse(url) # ParseResult object as Tuple
    print("Details from ParseResult object")
    print(parsed)
   
def saveContents(urlToRead, destFile):
    from urllib import request
    outFile = open(destFile,"wb")
    try:
        with request.urlopen(urlToRead) as response:
            data = response.read()
            outFile.write(data);
    except urllib.error.HTTPError as err:
        print(err)
    finally:
        if(not outFile.closed):
            outFile.close()   
    
if __name__ == '__main__':
    
    encode_url_demo()
    # url = 'http://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
 
    # url = 'https://hi.wikipedia.org/wiki/' 
    # url ='https://hi.wikipedia.org/wiki/%E0%A5%A8%E0%A5%AF_%E0%A4%9C%E0%A4%A8%E0%A4%B5%E0%A4%B0%E0%A5%80'
    # url= 'https://en.wikipedia.org/wiki/India'
    # url= 'https://zh.wikipedia.org/wiki/%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91'
    # requestDemo(url)
    # readWebPage(url)
    # url = "https://www.york.ac.uk/teaching/cws/wws/webpage2.html"
    # url = urllib.parse.quote(url)
    # saveWebPage(url,"viraj.html")
    # passingParameters()
    # https://www.google.com/search?q=pune
    # url_parse_demo('https://www.bing.com/search?q=pune')

    # url = 'https://github.com/robjhyndman/ETC3550Slides/raw/fable/1-getting-started.pdf'
    url =  "https://www.monash.edu/business/ebs/research/publications/ebs/wp20-2021.pdf"
    
    # url_parse_demo(url)
   
    saveContents(url,"paper1.pdf")
    # url = "https://file-examples.com/storage/feb57324aa650f65fa00875/2017/11/file_example_MP3_700KB.mp3"
    # saveContents(url,"song.mp3")

    