clothes = [int(x) for x in input().split()]

rack_capacity = int(input())

racks_count = 1 if clothes else 0
current_rack_capacity = rack_capacity

while clothes:
    current_clothing = clothes[-1]  
    
    if current_rack_capacity >= current_clothing:
        current_rack_capacity -= current_clothing
        clothes.pop()  
    else:
        racks_count += 1
        current_rack_capacity = rack_capacity  

print(racks_count)