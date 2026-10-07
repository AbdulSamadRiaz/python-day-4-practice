subjects = ["programing", "Database", "Networking", "Mathematics", "English"]
print(subjects)
subjects[4] = "Software Engeenering"
print(subjects)
print(subjects[4])
subjects.append("Physics")
print(subjects)

marks = [90,70,80,85]
marks.append(60)
print(marks)


subjects = ["programing", "Database", "Networking",]
subject = input("Enter a subject: ")
subjects.append(subject)
print(subjects)

fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.remove("Mango")
fruits.append("Grapes")
print(fruits)

numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
numbers.pop()
print(numbers)


subjects = ["Programming", "Database", "Networking", "Mathematics"]
print(subjects)
print(len(subjects))
subjects.append("English")
print(len(subjects))


fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]
for fruit in fruits:
    print(fruit)
    

marks = [45, 78, 32, 90, 55]
for mark in marks:
     if mark>50:
          print(mark)
          

numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
print(total)


marks = [80, 75, 90, 65, 70]
total = 0
for mark in marks:
    total += mark
    average = total / 5
print(f"Total Marks:   {total}")
print(f"average Marks: {average}")

