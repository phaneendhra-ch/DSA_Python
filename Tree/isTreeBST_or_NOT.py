"""

Is given Tree is BST or Not
    -> Using Inorder Traversal we can predict whether the tree is BST or not

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

def inorder(root,li:list):

    """

    Name : inorder()
    Arguments : root node of tree, li: list
    Desp : If list is iin sorted order then tree is BST, else False
    Rtype: True/False

    """
    if root == None:
        return

    inorder(root.left,li)
    li.append(root.value)
    inorder(root.right,li)

    return True if li == sorted(li) else False


if __name__ == '__main__':

    root = Tree(7)
    insert(root,4)
    insert(root,9)
    insert(root,5)
    insert(root,8)
    insert(root,2)
    insert(root,11)
    insert(root,15)
    print(inorder(root,[]))
