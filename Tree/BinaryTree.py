"""

Binary Search Tree using Linked List
Author : Phaneendhra

"""
class Node:

    def __init__(self,value:int):
        self.value = value
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.head = None

    def insert(self,num):

        """
        Name : insert()
        Arguments: num:int
        Description : Inserts node with a num by foloowing BST rule
        Rtype:None
        """

        if self.head == None:
            self.head = Node(num)
            return
        else:
            tmp = self.head

            while(tmp):

                if num == tmp.value:
                    print("Cannot insert Duplicate values")
                    return

                if num < tmp.value :
                    if tmp.left == None:
                        tmp.left = Node(num)
                        return
                    else:
                        tmp = tmp.left
                else:
                    if tmp.right == None:
                        tmp.right = Node(num)
                        return
                    else:
                        tmp = tmp.right
        return

def inorder(RootNode):

    """
    Name : inorder()
    Arguments: RootNode -> Head for the linked list
    Description : Prints Inorder Traversal of BST
    Rtype:None
    """

    if RootNode == None:
        #print("Tree is empty")
        return
    else:
        inorder(RootNode.left)
        print(RootNode.value,end=" ")
        inorder(RootNode.right)
    return

def preorder(RootNode):

    """
    Name : preorder()
    Arguments: RootNode -> Head for the linked list
    Description : Prints Preorder Traversal of BST
    Rtype:None
    """

    if RootNode == None:
        #print("Tree is empty")
        return
    else:
        print(RootNode.value,end=" ")
        inorder(RootNode.left)
        inorder(RootNode.right)
    return

def postorder(RootNode):

    """
    Name : postorder()
    Arguments: RootNode -> Head for the linked list
    Description : Prints Postorder Traversal of BST
    Rtype:None
    """

    if RootNode == None:
        #print("Tree is empty")
        return
    else:
        inorder(RootNode.left)
        inorder(RootNode.right)
        print(RootNode.value,end=" ")
    return

def searchNode(RootNode,num):

    """
    Name : searchNode()
    Arguments: RootNode -> Head for the linked list
               num : int -> value to be searched for

    Description : Searches for the node by given specific value
    Rtype:None
    """

    if RootNode==None:
        print("Tree is empty/Number Doesnt Exists")
        return
    else:
        tmp = RootNode
        if (num<tmp.value):
            searchNode(RootNode.left,num)
        elif (num==tmp.value):
            print(f"{num} exists in the tree")
            return
        else:
            searchNode(RootNode.right,num)
        return

def minimunNode(RootNode):

    """
    Name : minimunNode()
    Arguments: RootNode -> Head for the linked list
    Description : Prints minimum value node
    Rtype:None
    """

    if RootNode == None:
        print("Tree is empty")
        return
    else:
        tmp = RootNode
        while(tmp.left!=None):
            tmp = tmp.left
        print(f"\n{tmp.value} is minimum node ")
        return

def maximumNode(RootNode):

    """
    Name : maximumNode()
    Arguments: RootNode -> Head for the linked list
    Description : Prints maximum value node
    Rtype:None
    """

    if RootNode == None:
        print("Tree is empty")
        return
    else:
        tmp = RootNode
        while(tmp.right!=None):
            tmp = tmp.right
        print(f"\n{tmp.value} is maximum node ")
        return

my_binary_tree = Tree()
my_binary_tree.insert(3)
my_binary_tree.insert(5)
my_binary_tree.insert(2)
my_binary_tree.insert(1)
my_binary_tree.insert(4)
my_binary_tree.insert(9)

inorder(my_binary_tree.head)   
#preorder(my_binary_tree.head)
#postorder(my_binary_tree.head)
minimunNode(my_binary_tree.head)
maximumNode(my_binary_tree.head)
searchNode(my_binary_tree.head,4)
