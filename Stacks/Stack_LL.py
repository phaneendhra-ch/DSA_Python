"""
Creating Stack Using Linked List
Author : Phaneendhra
"""

class Node:

    def __init__(self,value = None):
        self.value = value
        self.link = None

class LinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):             #creating class as an iter object
        tmp = self.head
        while tmp:
            yield tmp.value
            tmp = tmp.link

    def __repr__(self):             #representation of class, we can use print statement -> print(Stack)
                                    # here Stack is an object for class LinkedList
        str_ = ""
        tmp = self.head
        while tmp:
            str_+= str(tmp.value)+" "
            tmp = tmp.link

        return str_

    def push(self,num):

        if self.head == None:
            self.head = Node(num)
        else:
            newnode = Node(num)
            newnode.link = self.head
            self.head = newnode
        return

    def pop(self):

        if self.head == None:
            print("Stack is Empty!")
            return
        else:
            rmnode = self.head
            self.head = self.head.link
            print(f"{rmnode.value} has been popped")
            rmnode.link = None
            return

    def isEmpty(self):
        if self.head == None:
            print("True")
        else:
            print("False")
        return

    def peek(self):
        if self.head == None:
            print("Stack is Empty !")
            return
        else:
            print(f"Top Node is stack is {self.head.value}")
            return

    def delete_stack(self):

        self.head = None
        print("Stack Destroyed !")
        return

if __name__ == "__main__":

    Stack = LinkedList()
    Stack.push(1)       #push
    Stack.push(2)
    Stack.push(3)

    Stack.pop()         #pop
    Stack.peek()        #peek
    Stack.isEmpty()     #isEmpty

    #print stack
    print(Stack)
    Stack.delete_stack()    #delete entire stack
