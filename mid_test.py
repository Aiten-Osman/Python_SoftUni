biscuit_per_day = int(input())
number_of_employees = int(input())
total_biscuits = 0
biscuits_competing_factory = int(input())


for days in range(1, 31):
    if days % 3 == 0:
        total_biscuits += int((biscuit_per_day * number_of_employees) * 0.75)
    else:
        total_biscuits += biscuit_per_day * number_of_employees

print(f"You have produced {total_biscuits} biscuits for the past month.")

difference = abs(total_biscuits - biscuits_competing_factory)
if total_biscuits > biscuits_competing_factory:
    difference_percentage = (difference / biscuits_competing_factory) * 100
    print(f"You produce {difference_percentage:.2f} percent more biscuits.")
else:
    difference_percentage = (difference / biscuits_competing_factory) * 100
    print(f"You produce {difference_percentage:.2f} percent less biscuits.")

