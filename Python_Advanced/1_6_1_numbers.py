# Read the first sequence of unique integers from a single line
set_1 = set(map(int, input().split()))

# Read the second sequence of unique integers from a single line
set_2 = set(map(int, input().split()))

num_command = int(input())

for _ in range(num_command):
    command = input()
    
    if command.startswith("Add First"):
        elements = map(int, command.split()[2:])
        set_1.update(elements)
        
    elif command.startswith("Add Second"):
        elements = map(int, command.split()[2:])
        set_2.update(elements)
        
    elif command.startswith("Remove First"):
        elements = map(int, command.split()[2:])
        set_1.difference_update(elements)
        
    elif command.startswith("Remove Second"):
        elements = map(int, command.split()[2:])
        set_2.difference_update(elements)
        
    elif command == "Check Subset":
        print(set_1.issubset(set_2) or set_2.issubset(set_1))

print(", ".join(map(str, sorted(set_1))))
print(", ".join(map(str, sorted(set_2))))