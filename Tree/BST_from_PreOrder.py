"""

Construct a BST From PreOrder Traversal

Author : Phaneendhra

"""

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

    if num < root.value:
        if root.left == None:
            root.left = Tree(num)
        else:
            return insert(root.left,num)

    if num > root.value:
        if root.right == None:
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
    print(root.value,end=" ")
    inorder(root.right)

if __name__ == '__main__':

    preorder = [7,4, 2, 5, 9, 8, 11, 15]    # preorder list

    value = preorder.pop(0)             # first element is root node

    root = Tree(value)                  # root node

    while preorder!=[]:                 # pop out each element from beginning of the list and insert the popped element in BST
        value = preorder.pop(0)
        insert(root,value)              # call insert

    inorder(root)                       #call inorder, output : nodes in sorted order
