# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 06:59:09 2018

@author: Hrishikesh Pisal
"""

# Function Object -- Indirect Function Call

# Name echo assigned to function object
def show(message:str)->None:
    '''Simple Function to echo the content passed'''
    print(message.capitalize())
    return


if __name__ =='__main__':
    # Call object through original name
    show('DIRECT CALL')
    
    # Now display references the function too
    display = show 
    # Call object through name by adding ()
    display('INDIRECT CALL !') 
    
    #Function objects and their names are two separate concerns
    del show
    show('Direct call')  # Error; has been deleted
    display('INDIRECT CALL Second time!')  # Still points to same function object 
    
    ## Attribute __name__
    print(display.__name__)
    print(show.__name__)
    print(display.__doc__)
    print(display)
    display.__name__ = "Echo_Message"
    print(display.__name__)
    show = display;
    print(show.__name__)
    show("New MESSAGE")
    
