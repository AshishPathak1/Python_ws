# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:43:39 2020

@author: Hrishikesh Pisal
"""


# nested functions can access the variables of the enclosing scope. 
# However, at least in python, they are only readonly

def temperature(degCel:float)->str:
  
    ## Local: Helper Function
    def celsius2fahrenheit()->float: 
        # Variable of the surrounding environment 
        # is ReadOnly in Nested function
        # degCel = degCel + 1  #Error
        return 9 * degCel / 5 + 32

    farenheit =  celsius2fahrenheit() 
    return f" It's {farenheit}˚ Farenheit!"



def transmit_to_space(message:str)->None:
    
    #This is the enclosing function
    def data_transmitter():
        '''Knows how to transmit the data to space'''
        print(f"'{message.upper()}' transmitted to space")
        return

    data_transmitter()
    return
    
# end of function transmit_to_space
    

if __name__ == '__main__':
    # tempCel = float(input("Enter temperature in degree Celcius : "))
    # result = temperature(tempCel)
    # print(result)
    
    transmit_to_space("Test message")
    # data_transmitter()   # error
    # celsius2fahrenheit() # error




