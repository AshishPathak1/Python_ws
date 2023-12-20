# imperative style
def read_text_file_linewise(file_name:str)->None:
     # if no mode is specified, 'r'ead mode is assumed by default
    file = open(file_name) #opened the file for reading
    line_no = 1
    while True:
        # print('*')
        line = file.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        
    #   print(line.split("\n")[0])
        print(f"LineNo: {line_no} : {line}",end='')
        line_no += 1
    # end of while loop
    file.close() # close the file
    return
   
 # Pythonic way : Declartive style
def read_file_Linewise_using_enumerate(file_name):
    print("Contents of the file are as follows")
    # using for loop
    for line in open(file_name):
        print(f"\t{line}", end = "")
    
    print("\nContent of the file with line numbers")
    for lineno,line in enumerate(open(file_name),start=1):
        # print(f"LineNo: {line[0]} : {line[1]}",end='')
        print(f"LineNo {lineno} : {line}",end='')
    
def create_text_file_for_writing(file_name:str):
    return open(file = file_name, mode = 'w') # open for 'w'riting
    
def  write_to_file(file_name:str,poem:str)->None:
    """
     Args:
        file_name :file name
        poem (str): the content that is to be written to file.

    Returns:
        None.
    """
    file_object = create_text_file_for_writing(file_name)
    file_object.write(poem) # write text to file
    file_object.close()
    return
    
def read_entire_file_at_once(file_name:str)->str:
    '''
    Read the etire file at once and print the same
     Args:
        file_name (str): The name of the file to read.

    Returns:
        the content of the file.

    '''
    # if no mode is specified, 'r'ead mode is assumed by default
    file = open(file_name,"r") #opend the file for reading
    data = file.read()
    print(f"File content is :\n{data}")
    file.close()
    return data

    
if __name__ == '__main__':
    poem = """Programming is fun
When the work is done
if you wanna make your work also fun
use Python!\n"""

    file_name = input("Enter the file name to create : " )
    write_to_file(file_name, poem)
    read_entire_file_at_once(file_name)
    read_text_file_linewise(file_name)
    read_file_Linewise_using_enumerate(file_name)
    