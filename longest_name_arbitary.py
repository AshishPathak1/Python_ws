def find_longest_name(*names): 
    if not names:
        return None
    longest_name = max(names,key=len)
    longest_name_legnth = len(longest_name)
    return longest_name,longest_name_legnth

names_input = input("Enter names seprated by commas:")
names_list = names_input.split(',')

longest_name,length = find_longest_name(*names_list)

print( f"Longest name : {longest_name}")
print(f"Length of longest name :{length}")
