# os  — Miscellaneous operating system interfaces
# sys — System-specific parameters and functions


def realpath_demo(file_name):
    ''' os.path — Common pathname manipulations : 
        This module implements some useful functions on pathnames.'''
    import os
    # construct a path representing the file in the current directory;
    # It is an abstract path- representing existing or non-exsiting file
    filepath = os.path.realpath(file_name,strict=False)
    print("Path : ", filepath)
    
    # Return True if path refers to an existing path otherwise returns False
    isFilePresent =  os.path.exists(filepath)
    print("Is File present ? ",isFilePresent)
    
def check_if_file_dir_link(filename):
    import os
    filepath = os.path.realpath(filename,strict=True)
    
    # Return True if path is an existing regular file.
    if(os.path.isfile(filepath)):
        print(f"{filepath} : is representing a file")
    # Return True if path is an existing directory. 
    # This follows symbolic links,
    elif (os.path.isdir(filepath)):
        print(f"{filepath} : is representing a directory")
    
    # Return True if path refers to an existing directory entry 
    # that is a symbolic link.
    print(f"is {filepath} a shortcut : {os.path.islink(filepath)}")
    print(f"is {filename} a shortcut : {os.path.islink(filename)}")
    print()

def append_and_seek_demo(fileName):
    import os
 # Open a file 'a' :append + read and write
    file_obj = open(fileName, "a+")
 # Append to end of the file
    # file_obj.write("Python is interesting!\n")
    # os.SEEK_SET : 0 : begning of file
    # os.SEEK_CUR : 1 : current position in file
    # os.SEEK_END : 2 : end of the file
    position = file_obj.tell()
    print ("Current file position : ", position)
    # Reposition the file pointer by 0 bytes from the begining of the file
    file_obj.seek(0,os.SEEK_SET)
    # Check current position
    position = file_obj.tell()
    print ("Current file position : ", position)
    #read 10 character from the begining and repositions the file pointer
    string = file_obj.read(10)
    print ("Read String is : ", string)
    print ("Current file position : ", file_obj.tell())
    string = file_obj.read(10)
    print ("Read String is : ", string)
    print ("Current file position : ", file_obj.tell())
    string = file_obj.read(10)
    print ("Read String is : ", string)
    file_obj.seek(0, os.SEEK_CUR)
    print ("Current file position : ", file_obj.tell())
    # can't do nonzero cur-relative seeks
    # file_obj.seek(10, os.SEEK_CUR)
    print ("Current file position : ", file_obj.tell())
    # file_obj.seek(-15, os.SEEK_CUR)
     
    # reposition to end of the file
    # file_obj.seek(10, os.SEEK_END)
    # can't do nonzero end-relative seeks
    # file_obj.seek(-10, os.SEEK_END)
    
    # print ("Current file position : ", file_obj.tell())
    
    # skips the first 22 characters from the begining of the file
    file_obj.seek(22, os.SEEK_SET)
    string = file_obj.readline()
    print("Rest of the data after skipping 20 characters:\n",string)
    file_obj.close()


# Test this function on Command prompt and not in IDE
def file_descriptor_demo(filename):
    import os
 # Open a file 'a' :append + read and write
    file_obj1 = open(filename, "a+")
    
    print ("Initial file position : ", file_obj1.tell())
    file_desc1 = file_obj1.fileno()
    
    print(f"File descriptor : {file_desc1} {type(file_desc1)}")
    # file_obj.close()
    # Return an open file object connected to the file descriptor fd.
    file_obj = os.fdopen(file_desc1,"a+")
    file_desc = file_obj.fileno()
    os.lseek(file_desc, 21, os.SEEK_SET)
    print ("After skipping 21 position : ", file_obj.tell())
    line = os.read(file_desc,10)
    print('next  10 characters :',line.decode('utf-8'))
    print ("Position after read: ", file_obj.tell())
    
    # # negative seek possible using file descriptor
    os.lseek(file_desc, -10, os.SEEK_CUR)
    print ("Position after SEEK_CUR: ", file_obj.tell())
    line = os.read(file_desc,10)
    print('After repositioning  :',line.decode('utf-8'))
    print ("Position after read: ", file_obj.tell())
    
    os.lseek(file_desc, +25, os.SEEK_CUR)
    print ("Position after SEEK_CUR: ", file_obj.tell())
    line = os.read(file_desc,10)
    print("After moving 20 bytes ahead :",line.decode('utf-8'))
    
    #print last ten charaters of the file
    os.lseek(file_desc, -10, os.SEEK_END)
    print ("Position after SEEK_CUR: ", file_obj.tell())
    line = os.read(file_desc,10)
    print("Last ten characters of the file are :",line.decode('utf-8'))
    
if __name__ == '__main__':
    realpath_demo("tempfile.txt")
    # realpath_demo("tempfile1.txt")
    # realpath_demo("e:/temp/abc.txt")
    
    # check_if_file_dir_link("tempfile1.txt") # Regular file at current location
    # check_if_file_dir_link("India")         # Regular Directory at current location
    # check_if_file_dir_link("IOT")           # Link to Directory  on another drive
    # check_if_file_dir_link("ca.lnk")        # Link to a File in current directory
    # check_if_file_dir_link("tag.lnk")       # Link to file in another directory
    # check_if_file_dir_link("India123")      # Non-Existing
    
    # append_and_seek_demo("data_win.txt")
    # append_and_seek_demo("data_unix.txt")
    
    # file_descriptor_demo("data_unix.txt")