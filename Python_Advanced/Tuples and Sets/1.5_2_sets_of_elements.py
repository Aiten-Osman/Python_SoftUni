n, m = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(n):
    element = input()
    set1.add(element)

for _ in range(m):
    element = input()
    set2.add(element)

intersection = set1 & set2

for element in intersection:
    print(element)