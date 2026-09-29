n = int(input())

longest_intersection = set()

for _ in range(n):
    line = input() 
    
    parts = line.split("-")
    first_range_str = parts[0]  
    second_range_str = parts[1] 
    
    first_parts = first_range_str.split(",")
    first_start = int(first_parts[0])
    first_end = int(first_parts[1])
    
    second_parts = second_range_str.split(",")
    second_start = int(second_parts[0])
    second_end = int(second_parts[1])
    
    set1 = set(range(first_start, first_end + 1))
    set2 = set(range(second_start, second_end + 1))
    
    current_intersection = set1 & set2
    
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

sorted_result = sorted(longest_intersection)

result_text = ", ".join(map(str, sorted_result))

print(f"Longest intersection is [{result_text}] with length {len(longest_intersection)}")