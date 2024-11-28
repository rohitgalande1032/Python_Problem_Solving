def remove_adjacent(s):
    new_str = ""

    for i in range(len(s)):
        if i < len(s)-1 and s[i] == s[i+1]:
            i+=2  # Skip the duplicate pair
        else:
            new_str += s[i]

    return new_str

# def using_stack(s):
#     stack = []

#     for ch in s:
#         if stack and stack[-1] == ch:
#             stack.pop()
#         else:
#             stack.append(ch)
#     return "".join(stack)

print(remove_adjacent("abbcdd"))
# print(using_stack("aabbccdee"))