# It is easy and concise way to create list

# without using list comprehension
lst = []
for i in range(10):
    lst.append(i)

print(lst)

#using list comprehension
list = [x for x in range(10)]
print(list)

# print only even numbers
even = [x for x in range(10) if x%2 == 0]
print(even)

# add two if item is even
list = [x+2 for x in range(10) if x%2 == 0]
print(list)

# print cube if number is even
cube = [x**3 for x in range(10) if x%2 == 0]
print(cube)