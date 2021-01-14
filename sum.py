#!/usr/bin/env python3

# Created by Sean McLeod
# Created on January 2021
# This program computes the sum using a list

import random


def sum_calculator(list_of_numbers):
    # this functions calculates the sum

    sum = 0

    for counter in list_of_numbers:
        sum = sum + counter

    return sum


def main():
    # this function uses a list

    numbers_to_add = []

    print("This program adds up random numbers(0~100) if you enter how many "
          "numbers you would like to add")
    print("\n")

    # input
    how_many_numbers = input("How many numbers do you want to add?: ")
    print(" ")

    try:
        int_how_many_numbers = int(how_many_numbers)

        for loop_counter in range(int_how_many_numbers):
            single_random_number = random.randint(1, 100)
            numbers_to_add.append(single_random_number)
            print("The random number {0} is {1} ".format(loop_counter,
                                                         single_random_number))
        print("")

        # call functions
        addition = sum_calculator(numbers_to_add)

        # output
        print("The addition of the numbers are: {} ".format(addition))

    except Exception:
        print("Please enter a number")


if __name__ == "__main__":
    main()
