"""

Binary Search Tree in Python

Author : Phaneendhra

"""
from collections import deque           #for level order traversal

class Tree:

    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

def insert(root,num):

    """

    Name : insert()
    Arguments : num : int
    Desp : inserts node by following BST rule
    Rtype: None

    """

    if num == root.value:
        print("Cannot insert duplicate values")
        return

    if num < root.value:
        if root.left is None:
            root.left = Tree(num)
        else:
            return insert(root.left,num)

    if num > root.value:
        if root.right is None:
            root.right = Tree(num)
        else:
            return insert(root.right,num)
    return

def inorder(root):

    """

    Name : inorder()
    Arguments : root node of tree
    Desp : Prints the inorder traversal of tree
    Rtype: None

    """

    if root == None:
        return

    inorder(root.left)
    print(root.value,end = " ")
    inorder(root.right)

def preorder(root):

    """

    Name : preorder()
    Arguments : root node of tree
    Desp : Prints the preorder traversal of tree
    Rtype: None

    """

    if root == None:
        return

    print(root.value,end = " ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):

    """

    Name : postorder()
    Arguments : root node of tree
    Desp : Prints the postorder traversal of tree
    Rtype: None

    """

    if root == None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value,end = " ")

def findnode(root,num):

    """

    Name : findnode()
    Arguments : root node of tree, num:int
    Desp : Success,Searches for the node present in Binary Search Tree,else, Failure
    Rtype: None

    """
    if root is None:
        print("Tree is empty")
        return
    tmp = root
    while(tmp):
        if num == tmp.value:
            print(f"{num} is present in Binary Search Tree")
            return
        if num < tmp.value:
            tmp = tmp.left
        else:
            tmp = tmp.right

    print(f"{num} is not present in Binary Search Tree")

# Function to print level order traversal of a given binary tree
def levelOrderTraversal(root):

    # base case
    if not root:
        return

    # create an empty queue and enqueue the root node
    queue = deque()
    queue.append(root)

    # loop till queue is empty

    while queue:

        # process each node in the queue and enqueue their
        # non-empty left and right child

        curr = queue.popleft()

        #print(curr.value, end=' ')

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)

def get_minimum_node(root):

    """
    Name : get_minimum_node()
    Desp : Finds the Minimum value from BST
    Rtype : None

    """

    tmp = root
    if tmp:
        while(tmp.left):
            tmp = tmp.left
    else:
        print("Tree is Empty!")
        return
    print(f"Minimum node from BST : {tmp.value}")
    return

def get_maximum_node(root):

    """
    Name : get_maximum_node()
    Desp : Finds the Maximum value from BST
    Rtype : None

    """

    tmp = root
    if tmp:
        while(tmp.right):
            tmp = tmp.right
    else:
        print("Tree is Empty!")
        return
    print(f"Maximum node from BST : {tmp.value}")
    return


def minimum(root):

    """

    Name : minimum()
    Arguments : root: rootnode of the tree
    Description : Get minimum value from the right sub tree for deletion of a node in tree
    Rtype : node with max value

    """

    current = root

    while(current.left!= None):
        current = current.left

    return current

def deletenode(root,num):

    """

    Name : deletenode()
    Arguments : root: rootnode of the tree, num:int
    Description : deletes the node if found in Binary Search Tree
    Rtype : Updated Tree

    """

    if root == None:        # base root node if it is None
        print("Node Not Found/Tree is Empty")
        return root

    if num < root.value:
        root.left =  deletenode(root.left,num)

    elif num > root.value:
        root.right = deletenode(root.right,num)

    else:
        if num == root.value:

            # to check whether the left or right node is None or not

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # if neither the left or right is not None
            # here we can replace the node with maximum value of the left subtree
            # or else with the minimum value of the right sub tree

            temp = minimum(root.right)                              #get maximum value from right sub tree
            root.value = temp.value                                 #over ride the current node value with minimum value of its right sub tree
            root.right = deletenode(root.right,temp.value)          #now delete the minimum value from right subtree
                                                                    #as current node value got replcaed with minimum value of right subtree


    return root

def delete_tree(root):

    """

    Name : delete_tree()
    Arguments : root: rootnode of the tree
    Description : Deletes entire Binary Search Tree
    Rtype : None

    """

    root.value = root.left = root.right = None
    #return root

def height_tree(root):

    if root is None:
        return 0
    else:
        # Recursively call height of each node
        leftAns = height_tree(root.left)
        rightAns = height_tree(root.right)

        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1

if __name__ == '__main__':

    root = Tree(7)
    insert(root,4)
    insert(root,9)
    insert(root,5)
    insert(root,8)
    insert(root,2)
    insert(root,11)
    insert(root,15)
    get_minimum_node(root)
    get_maximum_node(root)
    #inorder(root)                          # inorder function
    #postorder(root)                        # postorder function
    #preorder(root)                         # preorder function
    #findnode(root,9)                       # findnode function
    levelOrderTraversal(root)               # level order traversal function
    root = deletenode(root,9)
    inorder(root)
    print(f"\nHeight of Binary Search Tree : {height_tree(root)}")
    #delete_tree(root)                      # Delete entire Binary Search Tree
