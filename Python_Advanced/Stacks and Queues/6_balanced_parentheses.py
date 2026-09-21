given_string = input()

parentheses = []

for char in given_string:
    if char == '(' or char == '[' or char == '{':
        parentheses.append(char)
    elif char == ')' or char == ']' or char == '}':
        if not parentheses:
            print("NO")
            break
            
        last_open = parentheses.pop()
        
        if char == ')' and last_open != '(':
            print("NO")
            break
        elif char == ']' and last_open != '[':
            print("NO")
            break
        elif char == '}' and last_open != '{':
            print("NO")
            break
else:
    if not parentheses:
        print("YES")
    else:
        print("NO")