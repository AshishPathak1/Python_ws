# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:09:11 2019

@author: Hrishikesh Pisal
"""

# Copying Binary File
# Copying text File
# Appending to text file

import os.path
import sys

def copyTextFile(srcFile:str,destFile:str):
    # Prompt the user to enter filenames
    srcFile  = srcFile.strip()
    srcFilePath = os.path.realpath(srcFile)
    # Check if source File file exists
    if not os.path.isfile(srcFilePath):
        print(f'{srcFile} is not a file')
        sys.exit(0)

    # Check in the  destination file path is correct
    destFilePath = os.path.realpath(destFile.strip())
    # if the destination file is already existing then create another
    # file as destination file (src_file_copy.ext)
    if  os.path.exists(destFilePath):
        print(f"{destFile} file path is already existing")
        name,ext = os.path.splitext(srcFilePath)
        destFilePath = os.path.realpath(name+"_copy"+ext)
        print(f"copying contents to file :{os.path.basename(destFilePath)}")
   
        
    # # Open files for input and output
    infile  = open(srcFilePath,  mode = "r")  #read
    outfile = open(destFilePath, mode = "w")  #write

    # # Copy from input file to output file
    countLines = countChars = 0
    for line in infile: #iterate through lines fron srcfile
        outfile.write(line)  # wrtite line to destfile
        countLines += 1
        countChars += len(line)
       
    print(f"{countLines} lines and {countChars}, chars copied")

    infile.close()  # Close the input file
    outfile.close() # Close the output file

#appends the contents of source file to end of destination file
def appendTextFile(srcFile,destFile):
    destFilePath = os.path.realpath(destFile)
    # Check if destFile file exists
    if not os.path.isfile(destFilePath):
        print(f"file {destFile} does not exists",file=sys.stderr)
        sys.exit(0)
    
    srcFilePath = os.path.realpath(srcFile)
    # Check if source File file exists
    if not os.path.isfile(srcFilePath):
        print(f"file {srcFile} does not exists")
        sys.exit(0)

    # Open files for input and output
    infile  = open(srcFilePath,  mode= "r")   #read   
    outfile = open(destFilePath, mode= "a")   #append

    # Copy from input file to output file
    countLines = countChars = 0
    for line in infile:
        outfile.write(line.upper())
        countLines += 1
        countChars += len(line)
       
    print(countLines, "lines and", countChars, "chars appended")

    infile.close()  # Close the input file
    outfile.close() # Close the output file
    
    
def copyImageFile(srcImage,destImage):
    try:
        with open(srcImage, mode = "rb") as srcFile, \
             open(destImage, mode = "wb") as destFile:
            while True:
                byte = srcFile.read(1)
                # print(byte)
                if not byte:
                    break
                destFile.write(byte) 
                # destFile.write(str(byte[0]).encode('utf-8')) #output.encode('utf-8')
        print("File has been copied")
    except FileNotFoundError as err:
        print(f"file : {err.filename} {err.strerror}",file=sys.stderr)
    except IOError as err:
        print(f"IO error with file {err.filename} {err.strerror}",file=sys.stderr)
        

# Not yet implemented in python
# def copyFile(srcFile,destFile):
#     import os
#     sfo = open(srcFile,"rb")
#     sfd = sfo.fileno()
#     sfo.seek(0,os.SEEK_END)
#     count = sfo.tell()
#     dfd = open(destFile,"wb").fileno()
#     os.copy_file_range(sfd,dfd, count)
#     sfo.close()
    
    

if __name__ == '__main__':
    src = input("Enter a source file: ")
    # print(len(src))
    dest = input("Enter a target file: ")
    # copyTextFile(src, dest)
    # appendTextFile( src, dest )
    copyImageFile(src,dest)
    # copyFile(src,dest)