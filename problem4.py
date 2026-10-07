student = {
    "name": "Samad",
    "age": 20,
    "university": "SMIU",
    "semester": 3
}
print(student)



student_marks=[90, 80, 76, 80, 82, 75]
total = 0

for total_marks in student_marks:
    total += total_marks
    average = total/  len(student_marks)

print(f"Total marks: {total}")
print(f"Average marks: {average}")

highest = student_marks[0]
lowest = student_marks[0]

for mark in student_marks:

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")

