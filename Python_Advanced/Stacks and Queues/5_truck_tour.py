from collections import deque

num_petrol_pumps = int(input())
petrol_pumps = deque()

for _ in range(num_petrol_pumps):
    petrol, distance = map(int, input().split())
    petrol_pumps.append((petrol, distance))

for i in range(num_petrol_pumps):
    current_petrol = 0
    success = True
    
    for petrol, distance in petrol_pumps:
        current_petrol += petrol
        if current_petrol < distance:
            success = False
            break
        current_petrol -= distance
        
    if success:
        print(i)
        break
        
    petrol_pumps.rotate(-1)