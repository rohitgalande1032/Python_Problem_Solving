# It is special type of function in python, that returns an iterable collection of items once at a time
# It is defined like regular function but use yield statement instead of return to yield values one at a time
# It produce value only when requested, which make it memory_efficient especially for large datasets
 
def creater():
    i=1
    while i<=10:
        yield i    #When generato function call yield it returns value and pause its execution
        i+=1
    
print(creater())
x=creater()
print(next(x))
print(next(x))     # When it called again it resumes execution right after the last yield statement