def get_pass_student_list(cutoff,**kwargs)->list:
    result = []
    for key,value in kwargs.items() :
        if value >= cutoff :
            result.append(key)
    return result
d = {}
n = int(input("Enter total number of students :"))
for i in range (n):
    key = input(f"Enter the name of {i + 1} student :")
    d[key] = float(input(f"Enter the percentage marks of {i+1} student :"))
ans = get_pass_student_list(32,**d)
print(ans)