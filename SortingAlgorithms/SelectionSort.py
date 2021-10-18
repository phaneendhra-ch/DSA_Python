"""
Selection Sort in Python
Author : Phaneendhra

Time Complexity : O(n*2)
"""

def selectionsort(arr):

    if arr == [] or len(arr) == 1:
        return "Cannot perform selection sort"

    for i in range(len(arr)):
        min_val = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_val]:
                arr[min_val], arr[j] = arr[j], arr[min_val]
    return arr

if __name__ == '__main__':

    arr = [4,2,1,0,3,6,8,7,9,5]
    print(f"Array after bubble sort : {selectionsort(arr)}")
