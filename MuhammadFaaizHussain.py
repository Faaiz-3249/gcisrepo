##Muhammad Faaiz Hussain UID:433002064


def triangle_validator(len1, len2, len3):
    """
    This function uses the parameters inputted from
    the function main() to calculate using selction
    satements and conditionals to see if the the triangle
    is valid or not and returns a boolean value of True if it is valid or False if not
    """
    # Selection Statement to make sure all condtions are met
    if (len1 + len2) > len3 and (len1 + len3) > len2 and (len2 + len3) > len1:
        return True
    else:
        return False


def main():
    """
    This function takes input from the user and selects them
    into the function triangle_validator() as the parameters for
    the fucntion to calculate wether the values given are proven to
    be a valid triangle or not. It returns an output of a boolean data type
    """
    # Input from the user
    len_in1 = int(input("Enter a length: "))
    len_in2 = int(input("Enter a length: "))
    len_in3 = int(input("Enter a length: "))
    # Plugging the variables as the parameters for the function
    print(triangle_validator(len_in1, len_in2, len_in3))


# Calling the fucntion main()
main()
