from collections import deque

food_quantity = int(input())

orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    current_order = orders[0]  
    
    if food_quantity >= current_order:
        food_quantity -= current_order
        orders.popleft()  
    else:
        break  

if not orders:
    print("Orders complete")
else:
  
    print(f"Orders left: {' '.join(str(x) for x in orders)}")




