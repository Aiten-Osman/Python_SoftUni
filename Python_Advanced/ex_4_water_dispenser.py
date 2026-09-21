from collections import deque

water_amount = int(input())
queue = deque()

while True:
    name = input()
    if name == "Start":
        break
    queue.append(name)

while True:
    command = input()
    if command == "End":
        break
    
    if command.startswith("refill"):
        liters = int(command.split()[1])
        water_amount += liters
    else:
        liters = int(command)
        person = queue.popleft()
        if water_amount >= liters:
            water_amount -= liters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

print(f"{water_amount} liters left")
