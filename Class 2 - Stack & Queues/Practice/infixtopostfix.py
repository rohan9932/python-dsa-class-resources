def priority(operator):
    if(operator == '^'):
        return 3
    elif(operator == '*' or operator == '/'):
        return 2
    elif(operator == '+' or operator == '-'):
        return 1
    else:
        return -1

def infixToPostfix(inputOrder):
    stack = []
    ans = ""

    for ch in inputOrder:
        #operands => then push to ans
        if ch.isalnum():
            ans += ch
        
        #opening brackets => push to the stack
        elif ch == '(':
            stack.append('(')

        #closing bracket => keep popping till '(' and add to ans
        elif ch == ')':
            #popping out till we get opening bracket
            while (stack and stack[-1] != '('):
                ans += stack[-1]
                stack.pop()
            stack.pop() #popping the opening bracket
        
        #operator handling
        else: 
            #set the higher priority operator to top
            #keep adding to stack till ch is not of higher priority than all as stack will have higher priority operator at top
            while(stack and priority(ch) <= priority(stack[-1])):
                ans += stack[-1] #adding the higher priority operator to ans
                stack.pop() #popping the higher priority operator
            
            stack.append(ch) #for empty stack directly add
                    

    while(stack):
        ans += stack[-1]
        stack.pop()

    return ans


print(infixToPostfix("a+b*(c^d-e)"))
