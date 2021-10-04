# nested function
# #method 1
""" def hello_function():
    def say_hi():      
        def say_hello():
            return "Hello"
        return say_hello
    return say_hi
hello = hello_function()
print(hello_function()) # return function say hi
print(hello_function()()) # return function say hi say hello
print(hello_function()()()) # return Hello
print(hello()()) # return Hello same """

# method 2 
""" def say_hello(a):
    return "Hello "+a

def say_hi(function):       
    return function("eiei")

def hello_function(function):
    return say_hi(function)

a = hello_function(say_hello)
print(a) # return Hello eiei """

# method 3 simple decorator
""" def say_hello(a):
    return "Hello " + a

def hello_function(function):
    def say_hi():
        func = function("eiei")  
        return func
    return say_hi()

decorate = hello_function(say_hello)
print(decorate) """

# method 4.1 use decorator (from 2)
""" def say_hi(function):       
    return function("eiei")

def hello_function(function):
    return say_hi(function)

@hello_function
def say_hello(a):
    return "Hello "+a

print(say_hello) """

# method 4.2 (from 3)
""" def hello_function(function):
    def say_hi():
        func = function("eiei")  
        return func
    return say_hi()

@hello_function
def say_hello(a):
    return "Hello " + a

print(say_hello) """

# method 4.3 (from 4.1)
def say_hi(function):       
    return function("eiei")

def hello_function(function):
    return function

@ say_hi
@ hello_function # not neccessary
def say_hello(a):
    return "Hello "+a

print(say_hello)
