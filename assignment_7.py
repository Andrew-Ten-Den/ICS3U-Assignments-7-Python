#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# This program combines two lists

import random


def merged(random_numbers1, random_numbers2):
    # this merges the two lists
    combined = []

    combined.append(random_numbers1[0])
    combined.append(random_numbers1[1])
    combined.append(random_numbers1[2])
    combined.append(random_numbers2[0])
    combined.append(random_numbers2[1])
    combined.append(random_numbers2[2])
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
