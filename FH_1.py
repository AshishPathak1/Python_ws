# File basic operation 

# Open a file file for writing
# Open file and return a corresponding file object. 
# 'w' mode creates a file if it is not existing 
#  otherwise truncates an existing file
fo = open("d:\\temp\\abc.txt", mode="w")
# Type of file
print("type : ", type(fo))

# write a string to a file
fo.write('Good Morning!\n')

# Close opened file
fo.close()

# check if the file has been closed
print('Has file been closed : ',fo.closed)

# open file for reading which is default mode (r)
fo = open(file="d:/temp/abc.txt")
print("type : ",type(fo))

# Default opening mode for the file
print("Mode : ",fo.mode)

# check if the file has been closed
print('Has file been closed : ',fo.closed)

# check encoding
print('encoding format for the file: ',fo.encoding)

# check errors setting
print('error setting for the file: ',fo.errors)

# check if the file has been closed
print('Has file been closed : ',fo.closed)

# check if the file has been closed
print('Has file been closed : ',fo.closed)

# check if the file is open
# print('Has file been open : ',fo.opened)


# check the file name
print('Name of the file: ',fo.name)

# read from the file till EOF
msg = fo.read()

# display the data read
print('Contents of the file is :',msg)

# close the file
fo.close()
