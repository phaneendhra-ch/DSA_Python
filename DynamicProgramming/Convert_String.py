"""

    Convert a string to another using delete,add and replace operations using Dynamic Programming - Top Down Approach

    Problem Statement:
        S1 and S2 are two strings
        Convert S2 to S1 using delete,add and replace operations

    Eg :
        S1 = "table"
        S2 = "tbrles"

        Explanation :

            Here, 'a' will be added at second position in S2
            'r' will be deleted from 'S2'
            's' will be deleted from 'S2'

            Total operations involved : 3

"""

def convert_string(index1,index2,string1,string2,dict_):

    if (index1 == len(string1)):                    # if we have reached to the end of s1
        return len(string2) - index2                # then delete the remaining elements from S2
                                                    # this can be fetched using len:S2 - current value of index2

    if (index2 == len(string2)):                    # if we have reached to the end of s2
        return len(string1) - index1                # then add the remaining elements of S1 to S2
                                                    # this can be fetched using len:S1 - current value of index1

    if (string1[index1] == string2[index2]):        #if we are at same characters( then increment index value of both string1 and string2 by 1)
        return convert_string(index1+1 ,index2+1 ,string1,string2,dict_)

    else:
        # here the index of the both strings plays a crucial role
        # now we noeed to store the value of both the index in the dict

        dict_key = str(index1)+str(index2)          # index value of both the string

        if dict_key not in dict_:

            delete_operation = 1 + convert_string(index1 ,index2+1 ,string1,string2,dict_)        # for delete then move S2 index to next one
            insert_operation = 1 + convert_string(index1+1 ,index2 ,string1,string2,dict_)        # for add then move S1 index to next one
            replace_operation = 1 + convert_string(index1+1 ,index2+1 ,string1,string2,dict_)     # for replace then move S1 and S2 index to next one

            dict_[dict_key] = min(delete_operation,insert_operation,replace_operation)            # returning the minimum operation

        return dict_[dict_key]                                                                    # return the value

if __name__ == '__main__':
    string1 = "table"
    string2 = "tbles"
    print(f"Minimum Operations required to convert S2 to S1 : {convert_string(0,0,string1,string2,{})}")

    # here a will be inserted , s will be deleted : 2 Operations
