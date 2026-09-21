info = input()
stack = []
for char in info:
    stack.append(char)
while stack:
    print(stack.pop(), end="")
