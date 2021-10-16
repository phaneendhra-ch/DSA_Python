"""
Creating Queue using List, follows FIFO rule
Author : Phaneendhra
"""

class Queue:

    def __init__(self):         #constructor
        self.queuelist = []

    def __repr__(self):         #representation, can use to print, Eg :print(my_queue)
                                #here my_queue is object for Queue
        if self.queuelist != None:
            return "\n".join(list(map(str,self.queuelist[::-1])))
        else:
            return ""

    def enqueue(self,num):      #method to add element in queue

        """
        Name : enqueue()
        Arguments : num :int
        Description : Appends the value to the list
        Rtype: None
        """

        self.queuelist.append(num)
        print(f"{num} has successfully inserted into queue")
        return

    def dequeue(self):          #method to remove first element from queue

        """
        Name : dequeue()
        Description : Removes the first value from the list
        Rtype: None
        """

        if self.queuelist == []:
            print("Queue is Empty!")
        else:
            print(f"{self.queuelist[0]} has successfully removed from Queue")
            self.queuelist.pop(0)       # here it removes the element at 0th index
        return

    def peek(self):

        """
        Name : peek()
        Description : Prints the Top element from queue
        Rtype: None
        """

        if self.queuelist == []:
            print("Queue is empty !")
        else:
            print(f"{self.queuelist[-1]} is current top value")
        return

    def isEmpty(self):

        """
        Name : isEmpty()
        Description : Returns True if Queue is empty, else, False
        Rtype: None
        """

        if self.queuelist == []:
            print("True")
        else:
            print("False")
        return

    def deleteQueue(self):

        """
        Name : deleteQueue()
        Description : Deletes entire queue
        Rtype: None
        """

        self.queuelist = None
        print("Queue has been Destroyed !!")
        return

if __name__ == "__main__":

    my_queue = Queue()
    my_queue.enqueue(5)     # add element to the list
    my_queue.enqueue(6)
    my_queue.enqueue(7)
    print(my_queue)         #print queue
    my_queue.peek()         #peek
    my_queue.dequeue()      #dequeue
    print(my_queue)
    my_queue.peek()
    my_queue.isEmpty()      #isEmpty
    my_queue.deleteQueue()
    print(my_queue)
