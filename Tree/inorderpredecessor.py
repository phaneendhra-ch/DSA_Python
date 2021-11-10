"""

Find Inorder predecessor of the given Node

Author : Phaneendhra


Algorithm :

    The inorder predecessor of a node

        if node.left!= None
            ->maximum value from its left subtree
        else
            node.left is inorder predecessor

Start with root,succ = NULL.

If node.value < root.value, root = root.left

If node.value > root.value, succ = root, root = root.right

If node.value == root.value and node.right != null, successor = minimum(root.right).

Return successor

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

def inorder_predecessor(root,succ,num):

    """

    Name : inorder_predecessor()
    Arguments : root : node of tree, succ : acts like parent node, num : inorder successor of num
    Desp : Prints the inorder successor of num
    Rtype: inorder successor of num, else NULL

    """

    if root == None:                    # if root is None
        return succ                     # return succ , if tree is empty it returns None

    if root.value == num:               # if given node exists in tree
        tmp = root

        if (tmp.left!=None):           # jump through its right subtree
            tmp = tmp.left
            while(tmp.right!=None):      # the minimal value is the inorder successor,so iterate unitl tmp.left is NULL
                tmp = tmp.right
            return tmp.value            # return inorder successor node value

    if (num < root.value):              # if num < root.value, and recursively call right subtree, here we dont update the succ

        return (inorder_predecessor(root.left,succ,num))

    if (num > root.value):               # if num > root.value, update succ at current root and recursively call left subtree
        succ = root                             # it is an exception if num > root.value
        return (inorder_predecessor(root.right,succ,num))

    return succ.value                   # return succ.value

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

if __name__ == '__main__':

    root = Tree(20)
    insert(root,9)
    insert(root,12)
    insert(root,5)
    insert(root,11)
    insert(root,14)
    insert(root,25)

    print(inorder_predecessor(root,None,9))
