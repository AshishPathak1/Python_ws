# using with command
# note the difference between readline and read
# note we are not closing the file explicitly

def with_stmt_demo1(filename):
    with open(filename) as my_file:
        #attempts to read the entire file at one go
        print(my_file.read())   #discards newline
  
def with_stmt_demo2(filename):
    with open(filename) as my_file:
        #readlines returns list of lines from the file
        print(type(my_file.readlines()))
        print(my_file.readlines())   #retains newline

def with_stmt_demo3(filename):
    
    try:
        with open(filename) as my_file:
            print(f"Is the file closed (inside with block)? : {my_file.closed}")   
            lines_list = my_file.readlines()
        
            print("type of lines_list :", type(lines_list))
            print()
            print("File Contents in list  are:\n",lines_list)
            print()
            print("The first two lines from file are:\n",lines_list[0],lines_list[1])
            print()
            print("All the lines from file are as follows :")
            for line in lines_list:
                print(f"\t{line}",end='')
            print(f"Is the file closed (inside with block) ? : {my_file.closed}")
            print()
        #File is closed automatically
        print(f"Is the file closed (outside with block) ? : {my_file.closed}")  
    except FileNotFoundError as err:
        import sys
        print(f"Error Occured!\n{err}\n",file=sys.stderr)
      

def with_stmt_demo4(filename):
    #using for
    with open(filename,mode="r") as my_file:
        # file objects in Python are iterable 
        for line in my_file:
            print(f"\t{line.upper()}",end= '')  

# with can be used to handle multiple files
def with_multiple_files1(file1,file2)->None:
    print(f"content of file {file1} & {file2}")
    with open(file1) as f1, open(file2) as f2:
        print(f"first {file1}")
        print(f1.read())
        print(f"\nSecond {file2}")
        print(f2.read())
   
# Support for using grouping parentheses to break the statement in multiple lines.
def with_multiple_files2(file1,file2)->None:
    print(f"content of file {file1} & {file2}")
    with (
            open(file1) as f1,
            open(file2) as f2
        ):
        print(f"first {file1}")
        print(f1.read())
        print(f"\nSecond {file2}")
        print(f2.read())        
        
if __name__ == '__main__':
    filename = 'poem.txt'
    # with_stmt_demo1(filename)
    # with_stmt_demo2(filename)
    # with_stmt_demo3(filename)
    # with_stmt_demo4(filename)
    # with_multiple_files1('poem.txt','song.txt')
    with_multiple_files2('poem.txt','song.txt')
  