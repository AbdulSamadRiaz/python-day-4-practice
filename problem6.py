def greet():
    print("Hello, Welcome to python! ")
greet()
greet()
greet()



def student_info():
   print("Name: Abdul Samad Riaz" \
   "\nuniversity: SMIU" \
   "\nSemester: 4")

student_info()


def check_even_odd(number):
    if number % 2 == 0:
        print("Even Number!")
    else:
        print("odd number!!")

check_even_odd(32)
check_even_odd(3)


def sum(a,b):
    return a+b
result = sum(12,90)
print(result)


def square(num):
    return num *num
result = square(9)
print(result)


def maximum(a,b):
    if a > b:
        return a
    else:
        return b
result = maximum(120,78)
print(result,"is maximum!")


def calculator(a,b,operator):
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        return a/b
    else:
        print("invalid operator!")

result = calculator(2,3,"/")

print(result)


def factorial(number):
    result = 1

    for i in range(1,number+1):
        result = result * i
    return result

answer = factorial(6)
print(answer)



def is_prime(number):
    if number < 2:
        return False
    for i in range(2,number):
        if  number % i == 0:
            return False
    return True
print(is_prime(13))