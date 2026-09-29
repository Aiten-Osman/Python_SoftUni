text = input()

char_counts = {}
for char in text:
    if char in char_counts:
        char_counts[char] += 1  
    else:
        char_counts[char] = 1  
sorted_chars = sorted(char_counts.keys())

for char in sorted_chars:
    count = char_counts[char]
    print(f"{char}: {count} time/s")