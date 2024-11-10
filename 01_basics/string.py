str = "Hello Rohit"

#Access Element
print(str[0])
#Print string
print(str)
#slicing start from 1 and end 5(exclusive)
print(str[1:5])
#last element of string -- called negative index
print(str[-1])
#Reverse string
print(str[::-1])
#print list of tuples with kay and value [(0, 'H), (1,'e), .......]
print(list(enumerate(str)))
#length of string
print(len(str))
#Memborship operator check character is present or not
print('l' in str)
print('l' not in str)
#concatinate string
print(str + str)
#multiply string
print(str * 4)