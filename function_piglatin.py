# Non-recursive implementation (NOT Recommended)
# def get_string1()->str :
#     inp_str = input("Enter a string :").split()
#     for i in inp_str :
#         if not i.isalpha() :
#             print("Enter only alphabets")
#             inp_str = get_string()
#     return inp_str

# Non-recursive implementation (Recommended)
def get_string()->str :
    while True :
        inp_str = input("Enter a string only alphabets :")
        if are_all_tokens_strings(inp_str):
            return inp_str
        print("String contains characters other than alphabets")
        
def are_all_tokens_strings(input_str:str)->bool:
    for token in input_str.split() :
        if not token.isalpha():
            return False
    return True
            
    
def piglatin(inp_str:str)->str :
    import typing 
    if not are_all_tokens_strings(inp_str):
        raise RuntimeError("The input to function piglatin should be a String containing on ")
    inp_list = inp_str.split()
    result = []     # Empty list
    SUFFIX:typing.FINAL[str] = "ay"
    for token in inp_list :
        str1 = token[:2]   # Extracts the first two letters from the token
        str2 = token[2:]   # Extracts all the letters from the token except for the first two 
        result.append((str2 + str1 + SUFFIX))
    return " ".join(result)

# Alternate implemetation using string instead of list
def piglatin1(inp_str:str)->str :
    import typing 
    if not are_all_tokens_strings(inp_str):
        raise RuntimeError("The input to function piglatin should be a String containing only alphabets ")
    result = str()   #Empty String
    SUFFIX:typing.FINAL[str] = "ay"
    for token in inp_str.split() :
        result = result + (token[2:] + token[:2] + SUFFIX) + " "
    return result   
    # token[:2]    # Extracts the first two letters from the token
    # token[2:]    # Extracts all the letters from the token except for the first two 
    
    
def piglatin2(input_str:str)->str:
    if not are_all_tokens_strings(input_str):
        raise RuntimeError("The input to function piglatin should be a String containing only alphabets ")
    result = str()
    for token in input_str.split() :
        result = result + get_token_piglatin(token) + " "
    return result   
    
def get_token_piglatin(string):
    import typing 
    SUFFIX:typing.FINAL[str] = "ay"
    return string[2:]+string[0:2]+SUFFIX
   
    
if __name__ == '__main__' :
    # input_str = get_string()
    # print(f"The Original String is : {input_str}")
    # print(f"The Piglatin of the input string is : {piglatin(input_str)}")
    print(f"The Piglatin of the input string is : {piglatin('This is second string')}")
    print(f"The Piglatin of the input string is : {piglatin1('This is second string')}")
  
    # print(f"The Piglatin of the input string is : {piglatin('This is 3rd string')}")    