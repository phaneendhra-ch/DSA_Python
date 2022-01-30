"""

    0/1 Knapsack Probelm using divide and conquer

    Intuition:
        It has few items based on its weight

        We need to find the maximum weight which can include all the items with the given capacity
"""

class Item():
    def __init__(self,profit,weight):
        self.profit = profit
        self.weight = weight


def zero_one_knapsack(items,capacity,currentindex):

    if (capacity<=0) or (currentindex<0) or (currentindex>= len(items)):        # if capacity < 0  currentindex<0 currentindex>= len(items)
        return 0

    elif items[currentindex].weight <= capacity:                                # if currentindex of item's weight is lees than capacity

        """
        Lets start from first item
            -> If we are starting from the first item then we need to add the first item profit
                and call the function recursively by subtracting the capacity with current items weight
                 and we can move to the next item
        """
        profit1 = items[currentindex].profit + zero_one_knapsack(items,capacity - items[currentindex].weight,currentindex+1)

        """
        Lets start from the second item
        """
        profit2 = zero_one_knapsack(items,capacity,currentindex+1)


        return max(profit1,profit2)         # retun the maximum of two profits

    else:
        return 0

if __name__ == '__main__':

    # Creating the instances for different fruits
    mango = Item(31,3)
    apple = Item(26,1)
    orange = Item(17,2)
    banana = Item(72,5)
    capacity = 7

    # Here find the capacity of 7 including all different fruits

    items = [mango,apple,orange,banana]

    print(f"Maximum Profit : {zero_one_knapsack(items,capacity,0)}")
