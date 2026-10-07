def name():
    print("Samad")
name()

def sum(a,b):
    return  a+b
addition = sum(9,3)
print(addition)


def info(name = "samad"):
    print("hello" ,name)

info()
info("Mohsin")

def calculate(a,b,c):
    return a+b+c , a*b*c
add,product = calculate(4,6,9)

print(add)
print(product)