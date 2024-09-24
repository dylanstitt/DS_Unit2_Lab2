##### Global color variables #####
from colorama import Fore

R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''


##################################


def TEST_private_attr(testArray):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Ensure attributes are private{W}\n")
    try:
        print(testArray.n)
        print(f"{W}Array size is private: {R}FAILED{W}")
    except:
        print(f"{W}Array size is private: {G}PASSED{W}")

    try:
        print(testArray.capacity)
        print(f"{W}Array capacity is private: {R}FAILED{W}")
    except:
        print(f"{W}Array capacity is private: {G}PASSED{W}")

    try:
        print(testArray.A)
        print(f"{W}Array contents is private: {R}FAILED{W}")
    except:
        print(f"{W}Array contents is private: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_private_methods(testArray):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Ensure methods are private{W}\n")
    try:
        testArray.resize()
        print(f"{W}Resize method is private: {R}FAILED{W}")
    except:
        print(f"{W}Resize method is private: {G}PASSED{W}")

    try:
        testArray.make_array(1)
        print(f"{W}Make array method is private: {R}FAILED{W}")
    except:
        print(f"{W}Make array method is private: {G}PASSED{W}")

    print("~" * 50, "\n\n")


def TEST_array_creation(testArray):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: New array generation{W}\n")

    test = len(testArray) == 0
    if test:
        print(f"New arrays contain ZERO elements: {G}PASSED{W}")
    else:
        print(f"New arrays contain ZERO elements: {R}FAILED{W}")

    test = testArray.get_cap() == 1
    if test:
        print(f"Default array capacity is ONE: {G}PASSED{W}")
    else:
        print(f"Default array capacity is ONE: {R}FAILED{W}")

    print(f"\nStart: {B}{testArray}{W}")

    test = str(testArray) == '[]'
    if test:
        print(f"Correct to-string method: {G}PASSED{W}")
    else:
        print(f"Correct to-string method: {R}FAILED{W}")

    print("~" * 50, "\n\n")


def TEST_add_elements(testArray):
    print("~" * 50)
    print(f"{P}TEST CATEGORY: Add elements to array{W}\n")

    print(f"Starting array: {B}{testArray}{W}")
    testArray.append("first")
    print(f"Array length 1: {B}{testArray}{W}\n")

    test = len(testArray) == 1
    if test:
        print(f"Size of array is updated: {G}PASSED{W}")
    else:
        print(f"Size of array is updated: {R}FAILED{W}")

    test = len(testArray) == testArray.get_cap() == 1
    if test:
        print(f"Array has reached capacity: {G}PASSED{W}")
    else:
        print(f"Array has reached capacity: {R}FAILED{W}")

    testArray.append("second")
    print(f"\nArray length 2: {B}{testArray}{W}\n")

    test = len(testArray) == 2
    if test:
        print(f"Size of array is updated: {G}PASSED{W}")
    else:
        print(f"Size of array is updated: {R}FAILED{W}")

    test = testArray.get_cap() == 2
    if test:
        print(f"Array capacity has doubled: {G}PASSED{W}")
    else:
        print(f"Array capacity has doubled: {R}FAILED{W}")

    testArray.append("third")
    print(f"\nArray length 3: {B}{testArray}{W}\n")

    test = len(testArray) == 3
    if test:
        print(f"Size of array is updated: {G}PASSED{W}")
    else:
        print(f"Size of array is updated: {R}FAILED{W}")

    test = testArray.get_cap() == 4
    if test:
        print(f"Array capacity has doubled: {G}PASSED{W}")
    else:
        print(f"Array capacity has doubled: {R}FAILED{W}")

    print("~" * 50, "\n\n")
