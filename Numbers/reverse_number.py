def reverseNumber(number):
    reversed_num = 0
    is_negative = number < 0
    number = abs(number)
    while number > 0:
        last_digit = number%10  #number % 10 gets the last digit of number
        reversed_num = (reversed_num * 10) + last_digit  #reversed_num * 10 + last_digit shifts reversed_num left by one position and adds the new digit
        number //= 10  #num //= 10 removes the last digit from num.
    return -reversed_num if is_negative else reversed_num #If num is negative, the function returns the reversed number as negative.


if __name__ == "__main__":
    number = int(input("Enter a Number "))
    print(f"Reverse of {number} is {reverseNumber(number)}")