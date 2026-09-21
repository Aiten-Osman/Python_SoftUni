expression = input()

stack = []

for i in range(len(expression)):
    char = expression[i]
    if char == '(' or char == '[' or char == '{':
        stack.append(i)
    
    elif char == ')' or char == ']' or char == '}':
        start_index = stack.pop()
        
        
        sub_expression = expression[start_index : i + 1]
        print(sub_expression)