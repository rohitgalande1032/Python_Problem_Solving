def checkPalindrome(string):
    left = 0
    right = len(string)-1

    while left < right:
        if string[left] != string[right]:
            return False
        left+=1
        right-=1
    return True

if __name__ == "__main__":
    string = "madam"
    print("Palindrome" if checkPalindrome(string) else "String is not Palindrome")

