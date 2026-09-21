n = int(input())

reservations = set()

for _ in range(n):
    code = input()
    reservations.add(code)

command = input()
while command != "END":
    if command in reservations:
        reservations.remove(command)
    command = input()

print(len(reservations))

for code in sorted(reservations):
    print(code)