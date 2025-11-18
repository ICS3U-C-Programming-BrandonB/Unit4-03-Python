#!/usr/bin/env python3

# Created By: Brandon
# Date: November 18th, 2025
# This program asks the user for the number and then calculates the power of two using a for loop


from math import factorial


def main():

    # get number from user
    number = input("Enter a whole number: ")

    # initialize counter and answer
    counter = 0
    answer = 0

    # Checking if the user entered an integer correctly
    try:

        number = int(number)
        print("You entered an integer!")

        # determine whether or the not the number is positive
        if number < 0:
            print("Please Enter a positive number")
        else:
            # uses a for loop to calculate the power of two
            for counter in range(number + 1):
                answer = 2**counter
                print("{}^2 = {}".format(counter, answer))

    except ValueError:
        print("That is not a valid integer")


# outputs the function
if __name__ == "__main__":
    main()
