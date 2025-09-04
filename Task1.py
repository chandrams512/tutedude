# Task 1

students = {
    "Manish" : 90,
    "Aarvi" : 95,
    "Manny" : 76,
    "Ravi" : 65,
    "Alice" : 85
}

student = input("Enter the student name: ")

if student in students:
    print(f"{student}'s marks: {students[student]}")
else:
    print("Student not found.")


