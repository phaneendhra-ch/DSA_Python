"""

To find out the Longest Repeated Sub Sequence for a string which occurs atleast twice.

Eg : "ATAKTKGGA"

     Here the Sub Sequent string = "ATKG" occurs more than twice

     Using Divide and Conquer Algorithm

"""

def Longest_common_subsequence_Twice(string_,current_index,last_index):

    if (current_index == (len(string_)-1)) or ((last_index == (len(string_)-1))):       # if both indexes reaches end of the string
        return 0

    if (string_[current_index] == string_[last_index]) and (current_index!=last_index):     # if current_index and last_index holds the same character but at different positions
                                                                                            # Eg : current_index = 0 last_index = 2,
                                                                                                # string[0] == string[2] = A
        #print(string_[current_index], string_[last_index])
        subsequence_string+= string_[current_index]
        return Longest_common_subsequence_Twice(string_,current_index+1,last_index+1) + 1   # increment the value by 1

    else:
        first = Longest_common_subsequence_Twice(string_,current_index,last_index+1)        # call from first index
        second = Longest_common_subsequence_Twice(string_,current_index+1,last_index)       # call next of first index

        lenth_value = max(first,second)
        return lenth_value

if __name__ == '__main__':

    string_ = "ATAKTKGGA"
    current_index,last_index = 0,0
    print(f"The Longest Repeated Sub sequence of {Longest_common_subsequence_Twice(string_,current_index,last_index)}")
