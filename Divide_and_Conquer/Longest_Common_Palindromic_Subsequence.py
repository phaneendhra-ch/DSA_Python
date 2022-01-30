"""

Problem Statement:

    To find the longest common palindromic subsequence
    using Divide and Conquer Method

    Eg:
        S1 = "elephant"
        Output : ele

        S1 = "ameewema"
        Output : ameeema

"""

def Longest_common_palindromic_subsequence(string1,
                                            index1,
                                            index2
                                            ):
        if index1 > index2:                      # if index 1 exceeds index 2
            return 0

        elif index1 == index2:                   # if index 1 and index 2 are at same level
            return 1

        elif string1[index1] == string1[index2]:                        # if index1 and index 2 chars are same then move index1 by 1 and decrement index2 by 1

            return 2 + Longest_common_palindromic_subsequence(string1,
                                                        index1+1,
                                                        index2-1
                                                        )
        else :

            option1 = Longest_common_palindromic_subsequence(string1,   # start from first char of string and last second char of string
                                                        index1,
                                                        index2-1
                                                        )
            option2 = Longest_common_palindromic_subsequence(string1,   # start from second char of string and last char of string
                                                        index1+1,
                                                        index2
                                                        )
            return max(option1,option2)

if __name__ == '__main__':
    string = "ameewema"
    str_len = len(string) - 1
    print(f"Longest common palindromic subsequence of {string} is : {Longest_common_palindromic_subsequence(string,0,str_len)}")
