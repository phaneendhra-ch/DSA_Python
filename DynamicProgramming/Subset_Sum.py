"""

Find Subset sum from the given list

Eg : [3, 34, 4, 12, 5, 2], Sum = 9
     Subset : (4,5)

"""

def SubsetSum(set,n,sum):

    subset =([[False for i in range(sum + 1)]
            for i in range(n + 1)])

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
         subset[0][i]= False

    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):


            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]

            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])

    return subset[n][sum]       # The row and column save the desired value

if __name__ == '__main__':

    li_ = [3, 34, 4, 12, 5, 2]
    sum = 9
    n = len(li_)
    print(f"The subset of list : {li_} is {SubsetSum(li_,n,sum)}")
