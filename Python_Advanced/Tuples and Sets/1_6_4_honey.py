from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
operators = deque(input().split())

total_honey = 0

while bees and nectar:
    current_bee = bees[0]        
    current_nectar = nectar.pop() 

    if current_nectar >= current_bee:
        current_bee = bees.popleft() 
        symbol = operators.popleft()  

        if symbol == "/" and current_nectar == 0:
            continue

        result = 0
        if symbol == "+":
            result = current_bee + current_nectar
        elif symbol == "-":
            result = current_bee - current_nectar
        elif symbol == "*":
            result = current_bee * current_nectar
        elif symbol == "/":
            result = current_bee / current_nectar

        total_honey += abs(result)

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")