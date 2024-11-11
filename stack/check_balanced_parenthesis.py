# Steps to Check for Balanced Parentheses

# 1. Traverse each character in the string.
# 2. If the character is an opening bracket (like (, {, or [), push it onto the stack.
# 3. If the character is a closing bracket (like ), }, or ]):
# 4. Check if the stack is empty. If it is, return False because there's no matching opening bracket.
# 5. Otherwise, pop the top element from the stack. If it doesn’t match the corresponding opening bracket, return False.
# 6. At the end of the traversal, if the stack is empty, all brackets are balanced. If it’s not empty, there are unmatched opening brackets.

#First Method
def balancedParenthesis(s):
    stack = []
    for it in s:
        if it == "(" or it == "[" or it == "{":
            stack.append(it)
        else:
            if len(stack) == 0:
                return False
        
            ch = stack[-1]
            stack.pop()
            
            if ( it==')' and ch=='(') or (it==']' and ch=='[') or (it=='}' and ch=='{'):
                continue
            else:
                return False
    return len(stack)==0

# Second Method
def balancedParaDict(expression):
    stack = []
    brackets = {')':'(', ']':'[', '}':'{'}

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif(char in brackets):
            if not stack or stack.pop() != brackets[char]:
                return False
    return len(stack) == 0



if __name__ == "__main__":
    s = "([{}])"
    
    is_balanced = balancedParenthesis(s)
    print(is_balanced)

    print(balancedParaDict(s))

