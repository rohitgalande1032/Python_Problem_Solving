import reverse_number   #import module from ./reverse_number
number = 12321

def checkPalindrome(number):
    return number == reverse_number.reverseNumber(number)

if __name__ == "__main__":
    print(f"Reverse of {number} is {reverse_number.reverseNumber(number)}")
    print("Palindrome" if checkPalindrome(number) else "Not Palindrome")