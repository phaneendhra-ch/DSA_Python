"""

Binary Heap in Python

    -> It is of two types : Max Heap and Min Heap
    -> All the levels are completely filled, except the last node(if possible).

    ->Max Heap :
        -> The root node is greater than the child nodes and recursively applies for all the sub trees

    ->Min Heap :
        -> The root node is lesser than the child nodes and recursively applies for all the sub trees

Min Binary Heap:

    All the nodes are completely filled but the last node is not filled
    It is not mandatory to be filled, it can be filled or many not be filled

        1

    3       6

 5    9   8


Array Representation : [X,1,3,6,5,9,8]
                        0,1,2,3,4,5,6

                        Left child  = 2*i           , i =level
                        Right Child = 2*i + 1

The left and Right child of 1 :
    ->level of 1  = 1
        Left child = 2*1 = array[2] = 3
        Right child = 2*1 + 1 = array[3] = 6

Author : Phaneendhra

"""

class BinaryHeap:

    def __init__(self,size):
        self.customlist = (size+1)*[None]   # Arrays of size+1 as 0th index contains NULL
        self.heapsize = 0                   # Heap size starts with 0
        self.maxsize = size + 1             # max size of the list

def peekBinaryheap(root):

    """

    Name : peekBinaryheap()
    Arguments : root : root node of the tree
    Desp : prints the First Node in the tree i.e. element at index 1
    Rtype : None

    """

    if root == None:
        print("Binary Tree is Empty")
        return
    else:
        print(f"{root.customlist[1]} is the First element")
        return

def sizeBinaryheap(root):

    """

    Name : sizeBinaryheap()
    Arguments : root : root node of the tree
    Desp : prints the size of the binary heap tree
    Rtype : None

    """

    if root == None:
        print("Binary Tree is Empty")
        return
    else:
        print(f"Size of Binary Heap : {root.heapsize}")
        return

def levelOrderTraversal(root):

    """

    Name : levelOrderTraversal()
    Arguments : root : root node of the tree
    Desp : Prints the level order traversal of the tree
    Rtype : None

    """

    if root ==  None:
        print("Binary Tree is Empty")
        return
    else:
        for i in range(1,root.heapsize+1):
            print(root.customlist[i])
        return

def heapifyBinaryTree(root,index):

    """

    Here the tree is of Minimum Binary Heap

    Name  : heapifyBinaryTree()
    Arguments : root: root of the tree and index
    Desp : Heapifies the tree until it meets Minimum Binray Heap Tree condition
    Rtype : None

    """

    if index<=1:                    # if index is 1 then return
        return
    parent_index = int(index/2)     # here the value of parent node is (index/2)


    # In Min Binary heap the value of child node > value of parent node
    # If above condition is failed then below if condition is executed
    # Here the Parent and Child are swapped

    if root.customlist[index] < root.customlist[parent_index]:
        temp = root.customlist[index]
        root.customlist[index] = root.customlist[parent_index]
        root.customlist[parent_index] = temp

    heapifyBinaryTree(root,parent_index)

def insertnode(root,data):

    """

    Name  : insertnode()
    Arguments : root : root if the tree
                data : node that obtains the data
    Desp : inserts the node in binary heap (minimum)

    """


    if root.heapsize+1 == root.maxsize:
        print("Binary Heap Tree is Full")
        return
    else:
        root.customlist[root.heapsize+1] = data         #insert node in the list by incrementing heapsize by 1
        root.heapsize += 1                              # also increment heap size as we inserted new node
        print("Node Inserted in the root node")
        heapifyBinaryTree(root,root.heapsize)           # call heapify method if Binary Heap is not in order.
        return

if __name__ == '__main__':

    my_binary_heap = BinaryHeap(5)
    insertnode(my_binary_heap,3)
    insertnode(my_binary_heap,2)
    insertnode(my_binary_heap,1)
    insertnode(my_binary_heap,4)
    levelOrderTraversal(my_binary_heap)
    #print(my_binary_heap.maxsize)
