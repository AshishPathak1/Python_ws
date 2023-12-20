##understand the class method decorator
##this example highlight the difference between
##the instance method and class method

class Sample(object):

    class_data = 99 # shared between all objects of the class

    def __init__(self):
        self.instance_data = 10
        
    def foo(self): # instance method
        print('Inside foo')
        print('Instance data = ', self.instance_data)
        print('Class data = ', self.class_data)
        print('I am ', self)

    @classmethod
    def baz(cls):
        print('Inside baz')
        # print('Instance data = ',cls.instance_data)
        print('Class data = ', cls.class_data)
        print('I am ', cls)

    @staticmethod
    def bar(msg):
        print('Inside bar')
        # print('Instance data = ', self.instance_data)
        # print('Class data = ', cls.class_data)
        print('bar says', msg)

if __name__ == '__main__':

#  instance methods
    # Sample.foo() #Error
    s = Sample()
    s.foo() # invoke the instance method    

##class methods
    s.baz() # class method invoked using object
    Sample.baz() # class method invoked using class

##static methods
    s.bar("hello") 
    Sample.bar("bye")
