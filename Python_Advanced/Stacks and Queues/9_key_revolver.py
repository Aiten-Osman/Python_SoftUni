from collections import deque

price_of_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))
value_of_intelligence = int(input())

bullets_fired = 0
current_barrel = 0

# 2. Симулация на стрелбата
while bullets and locks:
    bullet = bullets.pop()        
    lock = locks[0]              
    
    bullets_fired += 1
    current_barrel += 1
    
    if bullet <= lock:
        print("Bang!")
        locks.popleft()          
    else:
        print("Ping!")
        
    if current_barrel == size_of_gun_barrel and bullets:
        print("Reloading!")
        current_barrel = 0

if not locks:
    earned_money = value_of_intelligence - (bullets_fired * price_of_bullet)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

