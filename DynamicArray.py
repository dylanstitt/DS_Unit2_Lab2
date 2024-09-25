import ctypes

class DynamicArray:

    def __init__(self):
        """Creates the array with a default cap of 1"""
        self.__n = 0
        self.__capacity = 1
        self.__A = self.__make_array(self.__capacity)

    def __str__(self):
        """To-String"""
        if self.__n == 0:
            return "[]"

        out = '['
        for i, element in enumerate(self.__A):
            try:
                out += str(element) + ', '
                temp = self.__A[i + 1]
            except:
                break
        return out[:-2] + ']'

    def __len__(self):
        """Returns the length of the array"""
        return self.__n

    def __getitem__(self, index):
        """Return element at index"""
        if index <= 0 or index >= self.__n:
            raise IndexError("invalid index")

        return self.__A[index]

    def __make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()

    def __resize(self):
        """Changes the capacity of the array when we reach max capacity"""
        self.__capacity *= 2
        tempArr = self.__make_array(self.__capacity)

        for i, item in enumerate(self.__A):
            tempArr[i] = item
        self.__A = tempArr

    def append(self, element):
        """Add a new element to the array and increase __n + 1 and increase __capacity if needed"""
        if self.__capacity == self.__n:
            self.__resize()

        self.__A[self.__n] = element
        self.__n += 1

    def get_cap(self):
        """Returns the capacity of the array"""
        return self.__capacity
