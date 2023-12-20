# sys.stdin
# sys.stdout
# sys.stderr
# File objects used by the interpreter for standard input, output and errors:
# stdin is used for all interactive input (including calls to input());
# stdout is used for the output of print() and expression statements 
# and for the prompts of input();
# The interpreter’s own prompts and its error messages go to stderr.


def print_for_writing_to_file(file_name):
    '''Explore stdin, stdout, stderr and print() '''
    
    # sys — System-specific parameters and functions
    import sys
    print("first Line") # write to console by default sys.stdout
    
    #you can print to the file by adding the file= argument
    # output sent to stdout can be redirected
    print("second Line", file = sys.stdout)     # write to console
   
    # data sent ot sys.stderr cannot be redirected
    print("error message", file = sys.stderr)   # write to console
    
    file_object = open(file_name, mode="w")     # Create a new file for writing
    
    print("third Line",  file = file_object)     # write to File
    print("fourth Line", file = file_object)    # write to File
    print("fifth Line",  file = sys.stdout)      # write to Console
    # print can be used to write formatted data
    import cmath
    print(f"PI : {cmath.pi}" ,file = file_object)
    print(f"PI formatted : {cmath.pi:010.2f}" , file = file_object)
    file_object.close() #close the file
    return
    
    
def readFile(file_name):
    '''Read the file to print its data to console'''
    file_object = open(file_name, mode = "r") #open file for reading
    print('Content of the file are : ')
    
    #file objects are iterable
    for line_str in file_object:   #read one line at a time
        print(line_str, end='' )
        print(line_str.upper(),end='')
        
    file_object.close()    #close the file
    return

def tty_demo(file_name):
    # The isatty() method returns True if the file stream is interactive, 
    # example: connected to a terminal device. TeleTYpewriter
    from sys import stdin  # standard input stream
    if stdin.isatty():
        print("Input (stdin) comes from tty.")
    else:
        print("Input (stdin)  doesn't come from tty.")
        
    import sys
    if sys.stdout.isatty():
         print("Output (stdout) goes tty.")
    else:
         print("Output (stdout) doesn't go to tty.")
        
    fileObj = open(file_name, "r" )
    if fileObj.isatty():
        print("Input (file HDD) comes from tty.")
    else:
        print("Input (file HDD )doesn't come from tty.")
    
    return

if __name__ == '__main__':
    #file_name = "tempfile1.txt"
    # print_for_writing_to_file(file_name)
    # readFile('poem.txt')
    tty_demo("d:\\temp\\abc.txt")
