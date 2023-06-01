students_grades = {
    "Gloria": 90,
    "Dazai": 85,
    "Fedor": 92,
    "Atsushi": 88,
    "Akutagawa": 95
}
top_student = max(students_grades, key=students_grades.get)
print("Студент з найвищою оцінкою:", top_student)

