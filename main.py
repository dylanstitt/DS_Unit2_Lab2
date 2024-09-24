# Dylan Stitt
# Unit 2 Lab 2
# Dynamic Array Class

# Implementation & testing of the DynamicArray class

from DynamicArray import *
from array_tests import *
import os

'''
Testing details can be found in array_tests.py

ENSURE ALL TESTS PASS BEFORE SUBMITTING
'''


def main():
    testArray = DynamicArray()

    # TEST 1 - ensure private attributes
    # BEFORE TESTING: create class, __init__, __getitem__
    TEST_private_attr(testArray)

    # TEST 2 - ensure private methods
    # BEFORE TESTING: create __resize and __make_array
    TEST_private_methods(testArray)

    # TEST 3 - verify initial setup
    # BEFORE TESTING: __len__, get_cap, __str__
    TEST_array_creation(testArray)

    # TEST 4 - add elements to array
    # BEFORE TESTING: append, __resize, __make_array
    TEST_add_elements(testArray)


if __name__ == "__main__":
    os.system("cls")
    main()