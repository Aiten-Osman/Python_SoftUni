import re

count_of_inputs = int(input())
pattern = r"^!([A-Z][a-z][a-z]+)!:\[([A-Za-z]{7}[A-Za-z]+)\]$"
for i in range(count_of_inputs):
    input_string = input()
    match = re.search(pattern, input_string) 
    if match:
        command = match.group(1)  
        text = match.group(2)     
        turn_to_ascii = [str(ord(char)) for char in text]
        print(f"{command}: {' '.join(turn_to_ascii)}")
    else:
        print("The message is invalid")