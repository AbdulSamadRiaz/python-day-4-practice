def calculate_result(numbers):
    maximim = 0
    mininum = numbers[0]
    total = 0 
    for num in numbers:
       total += num
    average = total/len(numbers)
    for num in numbers:
        if num > maximim:
           maximim = num
    

    for num in numbers:
        if num < mininum:
            mininum = num
    

    return total,average,maximim,mininum

marks = [85,76,90,65,88]
total,average,maximim,minimum = calculate_result(marks)

print("Total:", total)
print("Average:", average)
print("Maximum:", maximim)
print("Minimum:", minimum)

