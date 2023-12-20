# regular Function

def bar():
    print("Inside a bar")
    counter = 1
    print("Counter = ", counter)
    counter =  counter + 1
    print("Counter = ", counter)
    counter =  counter + 1
    return counter

# simplest generator function
# Remebers the place from where it yielded last
def foo():
    print("Fun started to execute")
    yield 1
    print("Yielding next char value")
    yield 'A'
    print("Yielding float value")
    yield 12.4
    print("Yielding next value")
    yield 'Last'

# Generator functions remember the state of local variables 
def baz():
    print("Inside a baz")
    counter = 1
    yield counter
    counter =  counter + 1
    yield counter
    counter =  counter + 1
    yield counter

if __name__ == '__main__':
    x  = bar()
    print(f" x = {x}" )
    y  = bar()
    print(f" y = {y}" )
 
    x = foo()   # returns the generator object, doesnt call foo
    print(f"Type returned by foo() : {type(x)}")
    
    y = next(x) # yields 1
    print(f" y = {y}" )
    
    y = next(x) # yields A
    print(f" y = {y}" )
    
    y = next(x) #  yields 12.4
    print(f" y = {y}" )
    
    y = next(x) # yields last
    print(f" y = {y}" )
    
    # y = next(x) # fails stopiteration
    # print(f" y = {y}" )
    
    g1 = foo()
    g2 = foo()
   
    y = next(g1) 
    print(f" y = {y}" )
    
    y = next(g2) 
    print(f" y = {y}" )
   
    g3 = baz()
    
    y = next(g3)
    print(f" y = {y}" )

    y = next(g3) # g3.__next__()
    print(f" y = {y}" )

    y = next(g3)
    print(f" y = {y}" )
    
    y = next(g3)
    print(f" y = {y}" )
    
    for data in baz():
        print(data)