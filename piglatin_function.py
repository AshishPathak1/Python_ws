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
    if not isinstance(inp_str,str) :
        raise RuntimeError("The input to function piglatin should be a String ")
    inp_list = inp_str.split()
    result = []
    suffix_str = "ay"
    for token in inp_list :
        str1 = token[:2]   # Extracts the first two letters from the token
        str2 = token[2:]   # Extracts all the letters from the token except for the first two 
        result.append((str2 + str1 + suffix_str))
    return " ".join(result)
    
    
if __name__ == '__main__' :
    input_str = get_string()
    print(f"The Original String is : {input_str}")
    print(f"The Piglatin of the input string is : {piglatin(input_str)}")
        