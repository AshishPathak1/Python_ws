# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 08:00:28 2019

@author: Hrishikesh Pisal
"""

# shutil : High Level File Operations
import shutil
import os
import sys

def print_list(mylist:list)->None:
    print("The list contents are as follows")
    print("\n\t".join(mylist))
    # for item in mylist:
    #     print(f"\t{item}")
        
        
def listfile_demo():
     # Return a list containing the names of the files in the directory.
    print( os.listdir()) # lists current directory
    # print_list(os.listdir('.')) # lists current directory
    # print_list(os.listdir('..')) #lists the parent directory
    
    
    # print("Listing of files and directories")
    # print( "=>","\n=> ".join(os.listdir('.')))
    # print( "\n\t".join(os.listdir(path="d:/wkdir"))) # List specified directory

# Using scandir() instead of listdir() can significantly increase the 
# performance of code that also needs file type or file attribute information
def list_with_attributes()->None:
    for dir_entry in os.scandir(): # os.DirEntry
        if dir_entry.is_file():  # is_dir()
            ftype = 'File'
        else:
            ftype = 'Directory'
        print(f"{dir_entry.name}\t{ftype}")
        
        
def changing_listing_dir():
  
    #change the current working directory
    os.chdir("d:/python/programs/image")
    # Listing current directory
    print('\nList current directory:')
    print("\n".join(os.listdir('.')))
    input("Press a key..")
    
    # Listing sub directory
    print('\nList sub directory:' )
    path = os.path.realpath('..')+"\\proj"
    print("\n".join(os.listdir(path)))
    input("Press a key..")
    
    os.chdir("d:/python/programs/group/proj")
    print('\nList current sub-directory:')
    print("\n".join(os.listdir('.')))
    input("Press a key..")
     
    # Listing parent directory
    print('\nList parent directory:')
    print("\n".join(os.listdir('..')))
    input("Press a key..")
 


def create_dir():
    import os
    # define the name of the directory to be created
    path = "d:/temp/year"
    try:
        os.mkdir(path)
    except OSError: 
        print (f"Creation of the directory {path} has failed")
    else:
        print (f"Successfully created the directory {path}")
        
def create_dirs():
    import os

# define the name of the directory to be created
    path = "d:/temp/year/month/week/day/hour/min/sec"
    try:
        os.makedirs(path)
    except OSError:
        print (f"Creation of the directory {path} failed" )
    else:
        print (f"Successfully created the directory {path} ")
        
        
# in windows use "attrib" and in Linux use "chmod"
def file_metadata(file_name):
    # Get the status of a file or a file descriptor
    stat_info = os.stat(file_name)
    # st_mode :File mode: file type and file mode bits (permissions).
    mode = stat_info.st_mode
    print('  Mode (oct)   :', mode)
    import time
    # the time of creation on Windows
    print(f'\tCreated : {stat_info.st_ctime}')
    # the time of creation on Windows
    print(f'\tCreated : {time.ctime(stat_info.st_ctime)}')
    # # Time of most recent access expressed in seconds.
    print(f'\tAccessed: {time.ctime(stat_info.st_atime)}')
    # # Time of most recent content modification expressed in seconds.
    print(f'\tModified: {time.ctime(stat_info.st_mtime)}')
    # # The size of the file
    print(f'\tFileSize: {stat_info.st_size} bytes')
  
    # Creator of the file. (May be available on Mac OS)
    # print(f'\tCreater: {stat_info.st_creator} ')
    # print(f'\tRealFileSize: {stat_info.st_rsize} bytes')
        

def delete_file():
    """Deleting File"""
    fileToDelete = r"d:/temp/menu.py" #r"/mnt/d/Python/programs/b.py"
    try:
        os.remove(fileToDelete)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print(fnfe.strerror)
    else:
        print(f'file {fileToDelete} has been deleted')

# Copy a file to a new file in current directory only.
# shutil.copyfile(src, dst, *, follow_symlinks=True)
# Copy the contents (no metadata) of the file named src to a 
# file named dst and return dst in the most efficient way possible. 
# src and dst are path-like objects or path names given as strings.
def copyfile_demo():
    import pprint
    print("\nBefore Copying")
    try:
        pprint.pprint(os.listdir(path="e:/temp"))
        src    = "d:\stories.txt"
        # dest = "d:/wkdir/abc/debug/readyou.txt"
        dest   = "e:/temp/jaadu/story.txt"
    
        shutil.copyfile(src, dest)
        
        print("\nAfter Copying")
        pprint.pprint(os.listdir(path="e:/temp"))
    except FileNotFoundError as fnfe:
        print(f"{fnfe.filename} {fnfe.strerror}",file=sys.stderr)
        
  
def copy_metadata():
    # Copy File with Metadata(as much as possible)
    # make an exact clone of the file, along with the 
    # permissions and the metadata of a file
    try:
        print('SOURCE FILE:')
        src_file = r"E:\IOT\Papers\research.pdf"
        dest_file = "e:/temp/code.pdf"
        # Does not copy the metadata
        # shutil.copy(src_file, dest_file) # Without metadata but with permissions
        # shutil.copy2(src_file, dest_file)  # Without certain metadata & permissions
        shutil.copyfile(src_file, dest_file) # Without metadata and permissions
        print('source FILE:')
        file_metadata(src_file)
        print('DESTINATION FILE:')
        file_metadata(dest_file)
    except PermissionError as pe:
        print(pe)

def copyfile_to_dir():
    
 # Copy file from current directory to specified sub-directory
    # shutil.copy(src_file, dst_dir,*, follow_symlinks=True)
    # shutil.copy('wheel.py', 'proj')  #copies the file into the directory
    # Copy File from one directory to another directory
    # srcFile = r"e:\MySql\V37661-01.zip"
    # destDir = r"e:\temp\abcd.zip"
    # shutil.copy(srcFile,destDir)  
    srcFile = r"e:\temp\code.pdf"
    destDir = r"e:\testing"
    shutil.copy(srcFile, destDir, follow_symlinks=True)
    # 


# Recursively copy an entire directory tree rooted at src to a 
# directory named dst and return the destination directory
def copy_directory():
    import glob
    import pprint
    import shutil
    # Replicate a directory tree recursively.
    srcDir_absolute_path  = r"d:/python/programs/cprog"
    destDir_absolute_path = r"d:/python/programs/cprog_bak"
    
    print('BEFORE:')
    pprint.pprint(glob.glob(srcDir_absolute_path))
    try:
        shutil.copytree(srcDir_absolute_path,destDir_absolute_path)  
        print('\nAFTER:')
        pprint.pprint(glob.glob(destDir_absolute_path))
    except FileExistsError as err:
          print(err)
         
    srcDir_relative_path  = r'../shutil' 
    destDir_relative_path = r'../tmp/example'        
    print('BEFORE:')
    pprint.pprint(glob.glob(srcDir_relative_path))
    try:
        shutil.copytree(srcDir_relative_path, destDir_relative_path )
        print('\nAFTER:')
        pprint.pprint(glob.glob(destDir_relative_path))
    except FileExistsError as err:
          print(err)  

    
# create the shortcut using operating system command like mkink
def copysymlink_demo():
    try:
        # copy with symlinks (default is follow_symlinks=True)
        # shutil.copyfile('e:/test/read.lnk', 'readlink.txt')
        # C:\Program Files\Spyder\spyder.ico
        shutil.copyfile(R"d:\\Python\\programs\\myspyder.lnk", 
                        R'F:\TEMP\myspyder.ico',
                        follow_symlinks=True)
        print("is src a link ? ",os.path.islink(R"d:\\Python\\programs\\myspyder.lnk"))
        print("is dest a link ? ",os.path.islink(R'F:\TEMP\myspyder.ico'))
        # shutil.copyfile('d:/titan.lnk', 'd:/wkdir/titan.csv')
    except FileExistsError as fee:
        print(fee.strerror)
    except FileNotFoundError as fnfe:
        print(fnfe.strerror)
        
def move_file():
    srcFile = r"d:/python/programs/research.pdf"
    destDir = r"f:/Temp"
    try:
        # Moving File
        shutil.move(srcFile,destDir)   
    except FileNotFoundError as err: # source file not found
        print(err)
    except shutil.Error as err:  # Destination path already exists
        print(err)
    else:
        print("Success! file has been moved!")

    
def move_dir():
    srcDir = "d:/python/programs/cprog_bak"
    destDir = "f:/temp"
    try:
        # Moving Directory
        shutil.move(srcDir,destDir)
    except FileNotFoundError as err: # source file not found
        print(err)
    except shutil.Error as err:  # Destination path already exists
         print(err)
    else:
        print("Success! Directory has been moved!")
 
# Delete an entire directory tree; path must point to a directory
def delete_dir():
    '''Deleting Directories'''
    # dirToDelete = "e:/temp/pack_copy1"
    dirToDelete = r"F:\TEMP\CPROG_BAK"
    try:
        # removing Director
        # shutil.rmtree(dirToDelete)
        # If ignore_errors is true, errors resulting from failed removals will be ignored;
        shutil.rmtree(dirToDelete,ignore_errors=True)
    except FileNotFoundError as err: # source file not found
        print(err)
    else:
        print("Success! Directory has been removed!")

# Finding files
# Return the path to an executable 
def find_files():
    import pprint
    # tells the path to an executable application which 
    # would be run if the given cmd was called.
    # print(f'The file location is : {shutil.which("g++")}')
    print(shutil.which('venvlauncher'))
    # When no path is specified, the results of os.environ() are used
    pprint.pprint(os.environ["path"])   
    print(shutil.which('venvwlauncher',path='D:\Python\Programs'))
    pprint.pprint(os.environ["path"])   
    # print(shutil.which('venvwlauncher'))
    # print(shutil.which('python.exe'))
 

# os.removedirs('foo/bar/baz') 
# will first remove the directory 'foo/bar/baz', 
# and then remove 'foo/bar' and 'foo'
       
def delete_directory():
    # import shutil
    # define the name of the directory to be deleted
    path = r"E:\temp\Company"
    path = "E:\\temp\\year\\month\\week\\day\\hour"
    
    try:
        # os.rmdir(path)     #deletes single empty directory
        os.removedirs(path)  #recursively deletes empty directory  
        # shutil.rmtree(path) #recursively deletes directory  
    except OSError:
        print ("Deletion of the directory %s failed" % path)
    else:
        print ("Successfully deleted the directory %s" % path)
 
#Monitoring File-system Space
def filesys_space():
    # print(shutil.disk_usage('.'))  # returns shutil.usage
    
    # total_b, used_b, free_b = shutil.disk_usage('.')
    total_b, used_b, free_b = shutil.disk_usage('C:')
    gb = 10 ** 9
    
    print('Total: {:6.2f} GB'.format(total_b / gb))
    print('Used : {:6.2f} GB'.format(used_b  / gb))
    print('Free : {:6.2f} GB'.format(free_b  / gb))



# Copy the permission bits from src to dst. 
# The file contents, owner, and group are unaffected. 
# shutil.copymode(src, dst, *, follow_symlinks=True)
# src and dst are path-like objects or path names given as strings.  
def copy_permisions1():       
    import os
    # import shutil
    
    with open('file1.txt', 'wt') as f:
        f.write('content')
        
    # os.chmod('file1.txt', 0o1350)
    
    print('BEFORE:', oct(os.stat('file1.txt').st_mode))
    print('BEFORE:', (os.stat('file1.txt').st_mode))
    
    shutil.copymode('area.py', 'file1.txt')
    
    print('AFTER :', oct(os.stat('file1.txt').st_mode))
    
def show_file_info(filename):
    import os
    import shutil
    import time
    stat_info = os.stat(filename)
    print('  Mode    :', oct(stat_info.st_mode))
    print('  Created :', time.ctime(stat_info.st_ctime))
    print('  Accessed:', time.ctime(stat_info.st_atime))
    print('  Modified:', time.ctime(stat_info.st_mtime))    
    
# To copy other metadata about the file use copystat().
# Only the permissions and dates associated with the file are 
# duplicated with copystat()
# Copy the permission bits, last access time, last modification time, 
# and flags from src to dst. On Linux, copystat() also copies the 
# “extended attributes” where possible. The file contents, owner, and 
# group are unaffected. src and dst are path-like objects or path names 
# given as strings.

def copy_permisions2():    
    import os
    import shutil
    
    with open('file2.txt', 'wt') as f:
        f.write('content')
    # os.chmod('file2.txt', 0o444)
    print('area:')
    show_file_info('area.py')
    print('file2 BEFORE:')
    show_file_info('file2.txt')
    
    shutil.copystat('area.py', 'file2.txt')
    
    print('file2 AFTER:')
    show_file_info('file2.txt')

if __name__ == '__main__':
    
    # os module
    # listfile_demo()
    # list_with_attributes()
    # changing_listing_dir()
    # create_dir()
    # create_dirs()
    # file_metadata(r"d:/temp/menu.py")
    delete_file()

    # shutil module
    # copyfile_demo()
    # copy_metadata()
    # copyfile_to_dir()
   
    # copy_directory()  
    # copysymlink_demo()
    # move_file()
    # move_dir()
   
    # delete_dir()
    # delete_directory()
    # find_files()
   
    # filesys_space()
    # copy_permisions1()
    # copy_permisions2()    