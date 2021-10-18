"""
Binary Seach in Python
Author : Phaneendhra

Time Complexity : O(logn)
Best Case : log(n)

"""

def BinarySearch(arr,num):

    left = 0                                            #base index
    right  = len(arr)-1                                 #last index

    while right>=left:                                  #while unitl right >= left

        mid = (left+right)//2                           #find mid value
        if (arr[mid] == num):                           # if arr[mid] == num,then value found
            return f"{num} is found at index : {mid}"

        if (arr[mid]<num):                              #decrement right by 1, if arr[mid] < num
            right = mid - 1

        else:                                           #increment left by 1, if arr[mid] > num
            left = mid + 1

    return f"{num} is not found"                        #return if num is not found


if __name__ == "__main__":
    
    arr = [5,6,7,8,9,1,2,4,0]
    search_value = 2
    print(BinarySearch(arr,search_value))
