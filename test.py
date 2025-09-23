##This program is used the calculate wether a users input is odd or even and
##Calculate what the squafre and the cube of the number is.


# input form the user
num1 = int(input("Enter a Number: "))


# Determine if the number is even or odd
def even_or_odd():
    """
    This fucntion uses Selection statements to determine
    wether the users input is even or odd
    """
    if num1 % 2 == 0:
        print("Number is even")
    else:
        print("Numberr is odd")


# square the input and cube aswell
def sqr_cube():
    """
    This Fcuntion uses arithermtic idetities of python sytax
    to calculate the squares and cubes of the users input
    """
    square = num1**2
    cube = num1**3
    print(square)
    print(cube)


# call the functions
def main():
    """
    This Fucntion calls the predetermined
    fucntions above to gain the outputs
    """
    even_or_odd()
    sqr_cube()
