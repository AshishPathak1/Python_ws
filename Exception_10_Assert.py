# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 10:08:46 2019

@author: Hrishikesh Pisal
"""

def apply_discount(product:dict, discount):
    
    discounted_price = 0
    
    if(product['price'] > 0):
        discounted_price = int(product['price'] * (1-discount))
    else:
        print("Invalid product Price")
  
    assert 0 <= discounted_price <= product['price'], "Discount Rate is incorrect" 
    
    return discounted_price


def apply_discount1(product, discount):
    #Never use Assertion of validation on function arguments
    assert product['price'] > 0 , "Invalid Product price"
    
    discountd_price = int(product['price'] * (1.0 - discount))
  
    assert 0 <= discountd_price <= product['price'], "Discount Rate is incorrect" 
    
    return discountd_price

if __name__ == '__main__':
    shoes = {'name': 'Shoes', 'price': 14500}
    
    print("discounted Shoe Price Rs: ",apply_discount(shoes, 0.3))
    
    pant = {'name': 'Pant', 'price': 4500}
    print("discounted Pant Price Rs : ",apply_discount(pant, 0.5))
    
    pant = {'name': 'Hat', 'price': 500}
    print("discounted Hat Price Rs : ",apply_discount1(pant, 0.5))

    pant = {'name': 'Jacket', 'price': -1500}
    print("discounted Jacket Price Rs : ",apply_discount1(pant, 0.4))
