num_of_students = int(input())
students_grades = {}

for _ in range(num_of_students):
    name, grade = input().split()
    grade = float(grade)
    
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for name, grades in students_grades.items():
    formatted_grades = " ".join([f"{g:.2f}" for g in grades])
    
    avg_grade = sum(grades) / len(grades)
    
    print(f"{name} -> {formatted_grades} (avg: {avg_grade:.2f})")