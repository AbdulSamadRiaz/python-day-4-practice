# write a program that finds both the highest and lowest marks using a for loop.

marks = [90, 50, 74, 65]
highest = marks[0]
lowest = marks[0] 

for mark in marks:

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")


