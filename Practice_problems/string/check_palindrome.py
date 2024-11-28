# def check_palindrome(s):
#     def reverse(s):
#         rev_str = ""
#         for ch in s:
#             rev_str = ch + rev_str
#         return rev_str
    
#     return reverse(s)==s

def check_palindrome(s):
    n = len(s)
    left=0
    right=n-1

    while left < right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1
    return True



result = check_palindrome("naman")
print("Palindrome" if result else "Not Palindrome")