def student_marks_lookup():
    student_marks = {
        "Alice": 85,
        "Bob": 78,
        "Charlie": 92,
        "David": 74
    }

    name = input("Enter the student's name: ")

    if name in student_marks:
        print(f"{name}'s marks: {student_marks[name]}")
    else:
        print("Student not found.")
if __name__ == "__main__":
    student_marks_lookup()