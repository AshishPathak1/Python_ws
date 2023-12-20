# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 13:24:37 2018

@author: Hrishikesh Pisal
"""
#working of finally
def calc_factorial(number_list:list)->None:
    import math
    for number in number_list:
        try:
            number_factorial = math.factorial(number)
        # Raised when an operation or function is applied to an object of inappropriate type    
        except TypeError:
            print(f"Factorial is not supported for input type '{type(number).__name__}'")
        # Raised when an operation or function receives an argument that has the right type but an inappropriate value,
        except ValueError:
            print("Factorial only accepts positive integer values.", 
                  number," is not a positive integer.")
        else: # when no error occurs
            print("The factorial of",number,"is", number_factorial)
        finally:
            print("Proceed to the next value in the list\n")
    else: # will be executed after termination of For Loop
        print("All elements in the list have been processed")
  
from decimal import Decimal 
# propogating an exception

def calc_discount(amt:Decimal, discount_rate:float)->Decimal:
    '''
    Parameters
    ----------
    amt : Decimal
        The Bill Amount for which discount is to be calculated.
    discount_rate : float
        Rate of discount

    Raises
    ------
    
        decimal.InvalidOperation.

    Returns
    -------
    Decimal
        Discount of type decimal.

    '''
    import decimal
    try:
        discount_rate = Decimal(discount_rate)
        if discount_rate < 0 :
            raise ValueError('discount rate cannot be -ve')
        amt = Decimal(amt)
        discount_amount =  amt * discount_rate / 100
        return discount_amount
    except ValueError as err:
        print(f"Error  :{err}")        
    except decimal.InvalidOperation:
        print("Invalid Operation! Data supplied could not be converted to decimal")
        raise  # re-raise
    return None

if __name__ == '__main__':
    import decimal
    # number_list = [3, 10, -5, 1.2, 'Ten', 4]
    # calc_factorial(number_list)
    # 
    # bill_amt = Decimal('4500.6')
    # discount_rate = 10.1    
    # bill_amt = "A4500"
    # discount_rate = 10.1
    # try:
    #     discount = calc_discount(bill_amt,discount_rate)
    #     if discount is not None:
    #         print(f'Discount Amount : Rs {discount:.2f}')
    # except decimal.InvalidOperation:
    #     print("Sorry the operation failed!")
    # except IndentationError:
    #     print("Incorrect indentation")
    # except SyntaxError:
    #     print("Incorrect indentation")
    
    # use case for handling SyntaxError : NEVER
    # try:
    #     import compileall
    #     compileall.compile_file('source.py')
    # except SyntaxError as err:
    #     print(f'ERROR {err}')
    
                            
    
    