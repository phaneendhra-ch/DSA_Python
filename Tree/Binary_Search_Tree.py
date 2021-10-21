class Tree:

    def __init__(self,value):
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
        print("Cannot insert duplciate values")
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
    Desp : Sucess,Searches for the node present in Binary Search Tree,else, Failure
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

if __name__ == '__main__':

    root = Tree(7)
    insert(root,4)
    insert(root,9)
    insert(root,5)
    insert(root,8)
    insert(root,2)
    insert(root,11)
    inorder(root)       #inorder function
    postorder(root)     #postorder function
    preorder(root)      #preorder function
    findnode(root,9)    #findnode function
