numbers_tuple = tuple(float(x) for x in input().split())

unique_numbers = ()

for num in numbers_tuple:
    if num not in unique_numbers:
        unique_numbers += (num,)

for num in unique_numbers:
    count = numbers_tuple.count(num)
    print(f"{num:.1f} - {count} times")
    