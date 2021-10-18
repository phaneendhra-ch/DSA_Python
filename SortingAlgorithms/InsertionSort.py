"""

Insertion Sort in Python
    -> Divide the array into two arrays
        ->First array is our original unsorted array
        ->second array is new array (Empty Initially)
    -> Take First Element from unsorted array and insert into new array by comparing each elements and place at resp index
    -> Repeat until original array is empty


Author : Phaneendhra


Time Complexity : O(n*2)
"""

def insertionsort(arr):

    if arr == [] or len(arr) == 1:
        return "Cannot perform insertion sort"

    for i in range(1,len(arr)):
        key = arr[i]            #current key
        j = i - 1               #previous element

        while j>=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j-=1
        arr[j+1] = key

    return arr

if __name__ == '__main__':
    arr = [4,2,1,0,3,6,8,7,9,5]
    print(f"Array after insertion sort : {insertionsort(arr)}")
