def sum_of_digits(num):
    sum = 0
    while num > 0:
        digit = num%10
        sum += digit
        num //= 10
    return sum

# sum of digits using recursion
def sum_of_digit(num):
    if num == 0: 
        return 0
    
    return (num%10) + sum_of_digit(num // 10)


print(sum_of_digits(1234))
print(sum_of_digit(1234))