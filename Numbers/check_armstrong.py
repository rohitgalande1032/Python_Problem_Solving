# An Armstrong number, also known as a narcissistic number or plenary number, is a number 
# that is equal to the sum of its own digits each raised to the power of the number of digits

def check_armstrong(num):
    n = len(str(num))
    original_num = num
    armstrong = 0
    while num > 0:
        digit = num % 10
        power = pow(digit, n)
        armstrong += power 
        num = num//10

    return armstrong == original_num

if __name__ == "__main__":
    num = 153
    print("Armstrong" if check_armstrong(num) else "Not Armstrong")
