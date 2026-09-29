from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk_cups = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    current_chocolate = chocolates[-1]
    current_milk = milk_cups[0]

    if current_chocolate <= 0 and current_milk <= 0:
        chocolates.pop()
        milk_cups.popleft()
        continue
    if current_chocolate <= 0:
        chocolates.pop()
        continue
    if current_milk <= 0:
        milk_cups.popleft()
        continue

    if current_chocolate == current_milk:
        chocolates.pop()
        milk_cups.popleft()
        milkshakes += 1
    else:
        milk_cups.rotate(-1)  
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if milk_cups:
    print(f"Milk: {', '.join(str(x) for x in milk_cups)}")
else:
    print("Milk: empty")