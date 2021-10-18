"""
Bubble Sort in Python
Author : Phaneendhra


Time Complexity : O(n*2)
"""

def bubblesort(arr):

    if arr == [] or len(arr) == 1:
        return "Cannot perform bubble sort"

    for i in range(len(arr)):               #compares each element with its successive element
        for j in range(i+1,len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == '__main__':

    arr = [4,2,1,0,3,6,8,7,9,5]
    print(f"Array after bubble sort : {bubblesort(arr)}")
