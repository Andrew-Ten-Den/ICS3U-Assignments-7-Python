#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# This program combines two lists

import random


def merged(random_numbers1, random_numbers2):
    # this merges the two lists
    combined = []
    # x and y represent the position in the list
    list_counter1 = 0
    x = 0
    list_counter2 = 0
    y = 0

    while list_counter1 < len(random_numbers1):
        combined.append(random_numbers1[x])
        list_counter1 = list_counter1 + 1
        x = x + 1

    while list_counter2 < len(random_numbers2):
        combined.append(random_numbers2[y])
        list_counter2 = list_counter2 + 1
        y = y + 1

    return combined


def main():

    random_numbers1 = []

    random_numbers2 = []

    loop_counter1 = 0

    loop_counter2 = 0

    print("Here are the 2 lists:")

    while loop_counter1 < 3:
        random_variable1 = random.randint(0, 100)
        random_numbers1.append(random_variable1)
        loop_counter1 = loop_counter1 + 1

    while loop_counter2 < 3:
        random_variable2 = random.randint(0, 100)
        random_numbers2.append(random_variable2)
        loop_counter2 = loop_counter2 + 1
    print("")

    print(random_numbers1)
    print(random_numbers2)
    # call function
    some_var = merged(random_numbers1, random_numbers2)

    print("\nHere is the combined list.\n")
    print(some_var)
    print("\nDone.")


if __name__ == "__main__":
    main()
