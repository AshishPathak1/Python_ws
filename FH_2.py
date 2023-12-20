# File Attributes

# Open a file
fo = open("d:/temp/abc.txt", mode = "r")
print ("Name of the file: ", fo.name)       # property
print ("Opening mode : ",    fo.mode)       # property
print ("Closed ? : ",        fo.closed)     # property
print ("Encoding: ",         fo.encoding)       # property
print ("Error setting: ",    fo.errors)       # property
print ("line buffering?: ",  fo.line_buffering)     # property

print ("File no : ",         fo.fileno())
fo.close()
print ("Closed ? : ",        fo.closed)

import sys
print ("stdout fileno : ",sys.stdout.fileno.__doc__)

