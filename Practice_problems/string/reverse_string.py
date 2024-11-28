# def reverse(s):
#     rev_string = ""
#     for ch in s:
#         rev_string = ch + rev_string
#     return rev_string



# def reverse(s):
#     return s[::-1]


def reverse(s):
    rev_string = ""
    n = len(s)+1
    for i in range(1, n):
        rev_string += s[-i]
    return rev_string


print(reverse("rohit"))