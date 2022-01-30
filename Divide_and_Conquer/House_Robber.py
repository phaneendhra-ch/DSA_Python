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

def max_amount(houses : list ,current_index : int):

    if current_index >= len(houses):                  #it indicates that index has reached the last element in the list
                                                      # Or, we have reached the last house / Array Bounding
        return 0

    else:
        print(f"Index : {current_index} : list size : {len(houses)}")
        steal_first_house = houses[current_index] + max_amount(houses,current_index+2)  # here we are considering the first house and calling the function by passing alternate index node
        skip_first_house = max_amount(houses,current_index+1)                           # here we are skipping the first index , so we are passing consecutive house index

        return max(steal_first_house,skip_first_house)                                  # here we are returining the maximum amount fetched

if __name__ == '__main__':

    house_list = [6,7,1,30,8,2,4]
    print(f"Maximum amount fetched : {max_amount(house_list,0)}")
