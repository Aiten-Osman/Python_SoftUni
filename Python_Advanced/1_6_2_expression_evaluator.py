expression = input().split()
stack = []

for sign in expression:
    if sign not in ("*", "+", "-", "/"):
        stack.append(int(sign))
    else:
        result = stack[0]
        
        for num in stack[1:]:
            if sign == "+":
                result += num
            elif sign == "-":
                result -= num
            elif sign == "*":
                result *= num
            elif sign == "/":
                result //= num
        
        stack.clear()
        stack.append(result)

print(stack.pop())