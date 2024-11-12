def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
     
    return fibonacci(num-1) + fibonacci(num-2)

# Print whole series up to that number
def fibonacci_series(num):
    num1 = 0
    num2 = 1
    list = []

    for _ in range(num):
        list.append(num1)
        num1, num2 = num2, num1+num2
    return list

print(fibonacci(8))
print(fibonacci_series(12))