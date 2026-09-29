from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

presents_table = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_presents = {}

while materials and magic_values:
    current_material = materials[-1]
    current_magic = magic_values[0]

    if current_material == 0 and current_magic == 0:
        materials.pop()
        magic_values.popleft()
        continue
    if current_material == 0:
        materials.pop()
        continue
    if current_magic == 0:
        magic_values.popleft()
        continue

    product = current_material * current_magic

    if product in presents_table:
        toy = presents_table[product]
        crafted_presents[toy] = crafted_presents.get(toy, 0) + 1
        materials.pop()
        magic_values.popleft()
    
    elif product < 0:
        total_sum = current_material + current_magic
        materials.pop()
        magic_values.popleft()
        materials.append(total_sum)
    
    elif product > 0:
        magic_values.popleft()
        materials[-1] += 15

is_successful = (
    ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or
    ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents)
)

if is_successful:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

for toy, count in sorted(crafted_presents.items()):
    print(f"{toy}: {count}")