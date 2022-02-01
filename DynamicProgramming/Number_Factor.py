"""

Number Factor in Python

Find Combinations of a number as a sum of 1,3,4

    Eg : 5
    Total no.of ways = 6
    (4,1) (1,4) (3,1,1) (1,1,3) (1,3,1) (1,1,1,1,1)

Involves both Top Down and Bottom Up Approach

Logic To remember b/w Top Down and Bottom Up

    -> In Top Down Approach, usage of recursive function will come in picture
    -> In Bottom Up Approach, there will be no recursive calls

"""

def number_factor(number : int ,dict_ : dict,type_ : str):

    # Top Down Approach
    if type_ == "TD":

        if number in [0,1,2]:
            return 1

        elif number == 3:
            return 2

        else:
             if number not in dict_:
                 part1 = number_factor(number-1,dict_,type_)
                 part2 = number_factor(number-3,dict_,type_)
                 part3 = number_factor(number-4,dict_,type_)
                 dict_[number] = part1 + part2 + part3

             return dict_[number]

    # Bottom Up Approach
    elif type_ == "BU":
        temp_arr = [1,1,1,2]        # for number = 0, number = 1, number = 2 and number = 3
        for i in range(4,number+1):
            temp_arr.append(temp_arr[i-1]+temp_arr[i-3]+temp_arr[i-4])

        return temp_arr[number]

    else:
        print("Enter a valid approach")

if __name__ == '__main__':

    print(f"Finding Number Factor using DP - Top Down {number_factor(5,{},'TD')}")
    print(f"Finding Number Factor using DP - Bottom Up {number_factor(5,{},'BU')}")
