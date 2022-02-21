"""

Maximum Length Chain Pair using Dynamic Programming

Given a set where {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90}}
    find the maximumlength chain pair whihc satisfies (a,b) (c,d) where, b<c

    Result :
    length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}

Time Complexity : O(n2)

"""

class Set():

    def __init__(self,a,b):
        self.a = a
        self.b = b


def maximumlength_chainpair(arr,n):

    # The main logice resides here
    # Here each Pair will create one chain
    # The max chain from here will be returned
    arr_max = [1 for each in range(n)]


    for i in range(1,n):                # iterate from 1st index to n (i)
        for j in range(0,i):            # iterate from 0 to i-1       (j)

            # since i is advanced then j, j = i+1
            # we will compare i.a with j.b (i.e., j.b < i.a)
            # i.e. (a,b) (c,d) --> b < c
            #        j     i
            if (arr[j].b < arr[i].a) and (arr_max[i] < arr_max[j]+1):       # keep track of outer loop chain value i.e. i
                arr_max[i] = arr_max[j]+1

    max_len = max(arr_max)  # return max from arr_max
    return max_len

if __name__ == '__main__':

    arr_set = [Set(5, 24), Set(15, 25), Set(27, 40), Set(50, 60)]
    #arr_set = [Set(5, 29), Set(39, 40), Set(15, 28), Set(27, 40), Set(50, 90)]

    print(f"Maximum Length Chain Pair : {maximumlength_chainpair(arr_set,len(arr_set))}")
