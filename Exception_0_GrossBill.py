# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 07:48:15 2018

@author: Hrishikesh Pisal
"""
import decimal
from decimal import Decimal

def getProductRate()->Decimal:
    while True:
        try:
            rate = Decimal(input("Enter the Product Rate (₹):"))
            if rate <= Decimal('0'):
                raise ValueError("The Product rate has to be a +ve integer!")
        except ValueError as err:
            print(f"Error message : {err}")
        except decimal.DecimalException:
            print("Format of Input is invalid!")
        # default 'except:' must be last
        except : #catch any exception that was not handled previously
            print('Unknown Error has occured')
        else:
            return rate

def getProductQuantity()->int:
    while True:
        try:
            qty = eval(input("Enter the Product Quantity :"))
            if not isinstance(qty, int):
                raise TypeError
            if qty <= 0:
                raise ValueError("The Product Quantity has to be a +ve integer in digits!")
        # Raised when an operation or function is applied to an object 
        # of inappropriate type
        except (TypeError, NameError) :
            print("Specify the Quantity in Numeric format only as integer")
        # Raised when an operation or function receives an 
        # argument that has the right type but an inappropriate value,
        except ValueError as err:
            print(f"Error Message :{err}")
        else:
            return qty
        
def getBillAmount(productRate:Decimal, productQty:int)->Decimal:
    billAmt = None
    try:
        if(productRate <= 0 or productQty <= 0):
            raise ValueError("Invalid Product Rate or Quantity supplied")
        billAmt = productRate * productQty    
    except ValueError as err:
        print("Error Message : ",err)
    except TypeError:
        print("Error: The Quantity and Product rate should be a numeric type")
    
    return billAmt
           
if __name__ == '__main__':
    productRate = getProductRate()
    # print(productRate)
    productQty  = getProductQuantity()
    # billAmt     = getBillAmount("Ten","Five")
    billAmt     = getBillAmount(productRate,productQty)
    # print(billAmt)
    if( billAmt is not None):
        print("Bill Amount is Rs :",billAmt)