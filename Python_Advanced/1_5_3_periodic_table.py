num_el = int(input())
set_elements = set()

for _ in range(num_el):
    elements = input().split()
    set_elements.update(elements)

print("\n".join(set_elements))