"""
Linear Search in Python
Author : Phaneendhra

Time Complexity : O(n)
"""


def LinearSearch(arr,value):
    for each in range(len(arr)):
        if arr[each] == value:
            return f"{value} found at index : {each}"
    return f"{value} is not found"


if __name__ == "__main__":

    a = [2,4,5,7,9,6,1]
    search_val = 6
    print(LinearSearch(a,search_val))
