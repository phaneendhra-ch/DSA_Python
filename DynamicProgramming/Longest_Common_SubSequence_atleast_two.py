"""

To find out the Longest Repeated Sub Sequence for a string which occurs atleast twice.

Eg : "ATAKTKGGA"

     Here the Sub Sequent string = "ATKG" occurs more than twice

     Dynamic Programming

Link : https://www.techiedelight.com/longest-repeated-subsequence-problem/

"""
#Top-Down
def Longest_common_subsequence_Twice_TopDown(string_,current_index,last_index,dict_):

    if (current_index == (len(string_)-1)) or ((last_index == (len(string_)-1))):       # if both indexes reaches end of the string
        return 0

    key = (current_index,last_index)

    if key not in dict_:

        if (string_[current_index] == string_[last_index]) and (current_index!=last_index):     # if current_index and last_index holds the same character but at different positions
                                                                                                # Eg : current_index = 0 last_index = 2,
                                                                                                    # string[0] == string[2] = A
            #print(string_[current_index], string_[last_index])
            dict_[key] =  Longest_common_subsequence_Twice_TopDown(string_,current_index+1,last_index+1,dict_) + 1   # increment the value by 1

        else:
            first = Longest_common_subsequence_Twice_TopDown(string_,current_index,last_index+1,dict_)        # call from first index
            second = Longest_common_subsequence_Twice_TopDown(string_,current_index+1,last_index,dict_)       # call next of first index
            dict_[key] = max(first,second)

    return dict_[key]


#Bottom_Up
def Longest_common_subsequence_Twice_BottomUp(string_,current_index,last_index):

    len_string = len(string_)

    dict_ = [[0 for x in range(len(string_))] for y in range(len(string_))]

    if (current_index == (len(string_)-1)) or ((last_index == (len(string_)-1))):       # if both indexes reaches end of the string
        return 0


    for i in range(0,len_string):
        for j in range(0,len_string):
            if dict_[i - 1] == dict_[j - 1] and i != j:
                dict_[i][j] = dict_[i - 1][j - 1] + 1
            else:
                dict_[i][j] = max(dict_[i - 1][j], dict_[i][j - 1])

    return dict_[len_string-1][len_string-1]

if __name__ == '__main__':

    string_ = "ATAKTKGGA"
    current_index,last_index = 0,0
    print(f"The Longest Repeated Sub sequence using DP- Top Down {Longest_common_subsequence_Twice_TopDown(string_,current_index,last_index,{})}")
    print(f"The Longest Repeated Sub sequence using DP- Bottom Up {Longest_common_subsequence_Twice_BottomUp(string_,current_index,last_index)}")
