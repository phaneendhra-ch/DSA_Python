"""

Create a Queue using Circular Linked List
Author : Phaneendhra

"""

class Node:

    def __init__(self, value = None):
        self.value =  value
        self.link = None

    def __repr__(self):
        return str(self.value)

class LinkedList:

    def __init__(self):            #constructor for class
        self.head = None
        self.tail = None

    def __iter__(self):            #enabling object as iterable
        tmp =self.head
        while tmp:
            yield tmp
            tmp = tmp.link

    def __repr__(self):             #representation of class, we can use print statement -> print(my_queue_LL)
                                    # here my_queue_LL is an object for class LinkedList
        str_ = ""
        tmp = self.head
        while tmp:
            str_+= str(tmp.value)+" "
            tmp = tmp.link

        return str_

    def enqueue(self,num):          #enqueue method

        if self.head == None:       #if head is None
                                    # then both head and tail hold same node
            self.head = Node(num)
            self.tail = Node(num)
        else:
            newnode = Node(num)        # craete instance of newnode
            tmp = self.head            # create instace of head
            while(tmp.link!=None):
                tmp = tmp.link          # iterate unitl last node
            tmp.link = newnode          # point last node to nenwnode
            self.tail = newnode         # tail holds new node
        return

    def dequeue(self):                  # dequeue

        if self.head == None:           #if head is None,then Queue linked list is empty
            print("Queue Linked List is empty!")
        else:
            if self.head == self.tail:     #if queue linked list has only one node to remove
                print(f"{self.head.value} has been removed !")
                self.head = None
                self.tail = None
            else:
                print(f"{self.head.value} has been removed !")
                self.head = self.head.link     #set head as head.link
        return

    def peek(self):                     #peek

        if self.head == None:           #if head is None,then Queue linked list is empty
            print("Queue Linked List is Empty!")
        else:
            #print top element from the queue linked list
            print(f"{self.tail.value} is current top element")
        return

    def isEmpty(self):              #isEmpty

        if self.head == None:        #if head is None,then Queue linked list is empty
            print("True")
        else:
            print("False")
        return

    def deleteQueue(self):          #deleteQueue

        #performs deletion of entire queue

        self.head = None
        self.tail = None
        return

if __name__ == "__main__":

    my_queue_LL = LinkedList()
    my_queue_LL.enqueue(5)          # add item in queue linked list
    my_queue_LL.enqueue(6)
    my_queue_LL.enqueue(7)
    print(my_queue_LL)              #print queue linked list
    my_queue_LL.dequeue()           #dequeue
    print(my_queue_LL)
    my_queue_LL.peek()              #peek
    my_queue_LL.deleteQueue()       #delete entire queue linked list
    print(my_queue_LL)
