"""
Merge Sort in Python
It follows divide and conquer method

Each block is divided into equal halves and it'll continue halfing recursively.

Later all the elements are stored in a sorted manner

Time Complexity : O(n*logn)
Author : Phaneendhra
"""

def mergesort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2     #Find out the mid value

    left = arr[:mid]      # left consists of index [0:mid]
    right = arr[mid:]     # right consists of index[mid:]

    mergesort(left)      #sort left array
    mergesort(right)     #sort right array

    return merge_two_sorted_lists(left, right, arr)    #return final sorted array

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)                      # length of left array
    len_b = len(b)                      # length of right array

    i = j = k = 0                       # indexing arrays,
                                        # i for left array, j for right array, k for combined

    while i < len_a and j < len_b:      #compare array elements from left to right and inserted them
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1                            #increment k

    while i < len_a:                  #if any leftout elements in left array after sorting
        arr[k] = a[i]                 #insert them into main array
        i+=1
        k+=1

    while j < len_b:                  #if any leftout elements in right array after sorting
        arr[k] = b[j]                 #insert them into main array
        j+=1
        k+=1
    return arr                        #return subarray after sorting
if __name__ == '__main__':
    arr = [4,2,1,0,3,6,8,7,9,5]
    print(f"Array after merge sort : {mergesort(arr)}")
