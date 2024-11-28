def valid_parenthesis(string):
    stack = []     #store opening perenthesis
    mapping = { ")":"(", "]":"[", "}":"{" }

    for char in string:
        if char in mapping:
            if stack:
                top = stack.pop()
                if top != mapping[char]:
                    return False
        else:
            stack.append(char)

    # If the stack is empty at the end, it's valid
    if not stack: 
        return True


string = "({[]})"
print("Valid" if valid_parenthesis(string) else "Not valid")