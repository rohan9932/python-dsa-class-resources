def isValid(s):
    stack = []

    for ch in s:
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch) #stack push
        else:
            if len(stack) == 0:
                return False
            elif (stack[-1] == '(' and ch == ')') or (stack[-1] == '{' and ch == '}') or (stack[-1] == '[' and ch == ']'):
                stack.pop() #stack pop
            else:
                return False
    
    return len(stack) == 0


str = "{([])}("
print(isValid(str))