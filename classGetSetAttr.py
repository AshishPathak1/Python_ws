## Understand the getattr() and setattr() methods

class Student:
    def __init__(self, name, rollNo, percentage):
        self.name = name
        self.roll = rollNo
        self.per  = percentage

    def __str__(self):
       return f"\nStudent {self.name} having Roll no : {self.roll} \
has secured {self.per} percentage marks"

# end of the class

if __name__ == '__main__':
    s1 = Student("Geeta", 10, 77.7)
    s2 = Student("Sanjay", 12, 74.7)
    
    print(s1)
    print('Name  :', s1.name)
    print('RollNo:', s1.roll)
    print('Name  :', getattr(s1, 'name', 'Not Known!'))
    print('RollNo:', getattr(s1, 'roll', "Unknown"))
    
    # AttributeError : 'Student' object has no attribute 'course'
    # print('Course:', s1.course) #Error
    # print('Course:', getattr(s1, 'course')) #Error
    print('Course:', getattr(s1, 'course',"Not yet taken")) #Okay

    print(s2)
#  bind attribute called course to objects s2
    s2.course = 'Python' 
    print('Course:', s2.course)
    print('Course:',getattr(s2, 'course', 'Not taken yet'))

##  bind attribute called course to objects s1
    setattr(s1, 'course', 'Advance Python')
    setattr(s1, 'name', "Geetanjali")
    print(s1)
    print('Course:', getattr(s1, 'course', 'Not taken yet'))
    print('Name:', s1.name)
    del s1.name ## removes the attribute from object
    # print('Name:',s1.name)
    print('Name:',getattr(s1, 'name', 'Attribute \'name\' not set'))
    print('Roll:',s1.roll)
    
