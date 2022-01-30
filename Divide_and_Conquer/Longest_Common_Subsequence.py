"""

Problem Statement:

    To find the longest common subsequence which is common to both strings
    using Divide and Conquer Method

    Eg:
        S1 = "elephant"
        S2 = "eaepant"

        Longest Common Subsequence : eepant

"""

def Longest_common_subsequence(string1,string2,index1,index2):

    if (len(string1) == index1):                                # if we have reached the end of string1 then return 0
        return 0

    if (len(string2) == index2):                                # if we have reached the end of string2 then return 0
        return 0

    if (string1[index1] == string2[index2]):                    # if both characters of string1 and string2 are equal,
                                                                # then move to the next character of the both strings
        return 1 + Longest_common_subsequence(string1,string2,index1+1,index2+1)

    else:
        start_string1 = Longest_common_subsequence(string1,string2,index1,index2+1)  # starting from first character of string1 and second character of string2
        start_string2 = Longest_common_subsequence(string1,string2,index1+1,index2)  # starting from first character of string2 and second character of string1

        return max(start_string1,start_string2)         # find maximum of both 

if __name__ == '__main__':
    string1 = "elephant"
    string2 = "eaepant"
    print(f"Longest Common Subsequence of {string1} and {string2} is {Longest_common_subsequence(string1,string2,0,0)}")
