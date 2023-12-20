import sys

start = input("Enter the start value :")
data = start.strip()

if data[0] in ['+','-'] :
    data = start[1::]

if not data.isdigit() :
    print("Enter valid Input",file=sys.stderr)
    sys.exit(0)
    
stop = input("Enter the stop value :")
data = stop.strip()

if data[0] in ['+','-'] :
    data = start[1::]

if not data.isdigit() :
    print("Enter valid Input",file=sys.stderr)
    sys.exit(0)

start =  int(start)
stop  =  int(stop)

step = -1
if start < stop :
    step = +1

    
dict = {}
print(start,stop,step)
for num in range (start,(stop+1),step):
    dict[num] = num**2
 
import pprint as pp
print("The dictionary is as follows :")
pp.pprint(dict,indent=5)
