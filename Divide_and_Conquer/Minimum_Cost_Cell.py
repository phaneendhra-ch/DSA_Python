"""

    Find the minimum cost to reach the last value of the cell using 2D array

    here each cell is associated with a value, find the minimum value to reach till the end

    Conditions :
    -> If you are in a cell then
        you can move to the right (or) down from the current cell

    Approach :
        Here we are moving from the last cell to top cell
        Now we can move left or up (revert condition)

"""


def minimum_cell_cost(array,row,col):
    if row==-1 or col==-1:
        return float('inf')

    elif row==0 and col==0:
        return array[0][0]

    else:
        op1 = minimum_cell_cost(array,row-1,col)        # move from same column to different rows (i.e. moving left)
        op2 = minimum_cell_cost(array,row,col-1)        # move from same row to different columns (i.e. moving up)

        return array[row][col] + min(op1,op2)       # here we need to alose return the current cell value

if __name__ == '__main__':

    array = [
            [4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3]
            ]

    print(f"Minimum Cost Cell from start to end : {minimum_cell_cost(array,4,4)}")
