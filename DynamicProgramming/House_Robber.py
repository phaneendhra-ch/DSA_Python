"""

House Robber in Python

Probelm Statement :

    A Robber can rob an house which contains money so that he cannot rob adjacent houses.

    Return Max Amount he can rob

    Eg :
        Money : 6   7   1   30  8   2   4

        If the robber enters first house(6Rs) he connot enter the second house i.e., (7Rs)

        Need to find the maximum Amount he can rob by satisfying the above conditions


"""
#Top Down
def max_amount_td(houses : list ,current_index : int,dict_ : dict):

    if current_index >= len(houses):                  #it indicates that index has reached the last element in the list
                                                      # Or, we have reached the last house / Array Bounding
        return 0

    else:

        if current_index not in dict_:
            steal_first_house = houses[current_index] + max_amount_td(houses,current_index+2,dict_)  # here we are considering the first house and calling the function by passing alternate index node
            skip_first_house = max_amount_td(houses,current_index+1,dict_)                           # here we are starting from the second index value

            dict_[current_index] = max(steal_first_house,skip_first_house)                        # add max value at the current index in dictionary

        return dict_[current_index]                                                               # return the dictionary value

#Bottom Up
def max_amount_bu(houses : list ,current_index : int):

    arr_store = [0]*(len(houses)+2)                                             # array consists all zeroes with (len+2) sized elements

    for each in range((len(houses)-1),-1,-1):                                   # as Bottom up approach we need to iterate fron last index to 0 -> (len(houses)-1) == last index

        start_first = houses[each] + arr_store[each+2]                          # if we are starting from first value
        start_second = arr_store[each+1]

        arr_store[each] = max(start_first,start_second)                         # if we are starting from second value

        #print(arr_store)                                                       # array modifies at each iteration
    return arr_store[0]                                                         # updated value will be at first index


if __name__ == '__main__':

    house_list = [6,7,1,30,8,2,4]
    print(f"Maximum amount fetched using DP - Top Down : {max_amount_td(house_list,0,{})}")
    print(f"Maximum amount fetched using DP - Bottom Up  : {max_amount_bu(house_list,0)}")
