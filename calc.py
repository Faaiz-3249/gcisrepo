def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def muliply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    a = int(input("Enter a num1: "))
    b = int(input("Enter a num1: "))
    print(f"addition: {add(a, b)}")
    print(f"subtraction: {subtract(a, b)}")
    print(f"multiplication: {muliply(a, b)}")
    print(f"division: {divide(a, b)}")


main()
##############################################################

num = int(input("Enter a num: "))

if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

#######################################################################
age = int(input("Enter age: "))

if age > 18:
    print("elligigble for voting")
else:
    print("not eligigble")


#######################################################################
def equal():
    a = int(input("Enter legnth: "))
    b = int(input("Enter legnth: "))
    c = int(input("Enter legnth: "))

    if a == b == c:
        print("triangle is equalateral")
    else:
        print("nuh uh")


equal()
