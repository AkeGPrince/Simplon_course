#CRUD
students = ["Hadi", "Hemon", "Forest", "Pauline"]

for student in students:
    print("Bonjour : " + student)
    print(f"Bonjour {student}")

upper_students = []
for student in students:
    upper_students.append(student.upper())
print(upper_students)

upper_students = [student.upper() for student in students]
print(upper_students)

for i in range(len(students)):
    print(f"{i+1}- Bonjour {students[i]}")

my_dict = {"Hadi" : "Male",
           "Hemon" : "Male",
           "Forest" : "Male",
           "Pauline" : "Female"}

for name,gender in my_dict.items():
    print(name, gender)
    print(f"{name} is {gender}")

i = 0
while i < len(students):
    print(f"{i+1}- Bonjour {students[i]}")
    i += 1
