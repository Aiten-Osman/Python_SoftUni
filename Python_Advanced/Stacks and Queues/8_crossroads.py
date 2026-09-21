from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

cars = deque()
total_cars_passed = 0

while True:
    command = input()
    if command == "END":
        break
    elif command == "green":
        green_light = green_light_duration
        free_window = free_window_duration
        
        while green_light > 0 and cars:
            car = cars.popleft()
            car_len = len(car)
            
            if car_len <= green_light:
                green_light -= car_len
                total_cars_passed += 1
            else:
                if car_len <= green_light + free_window:
                    total_cars_passed += 1
                    green_light = 0  
                else:
                    hit_index = green_light + free_window
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()
    else:
        cars.append(command)

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")