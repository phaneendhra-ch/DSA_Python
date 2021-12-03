"""

Single Linked List in Python

    -> Insertion
    -> Traversing
    -> Merge two linked list and sort them

Author : Phaneendhra

"""

class Node :
    def __init__(self,value =None):
        self.value = value
        self.link = None

class SLinkedList:
    def __init__(self): # constructor for the class
        self.head = None

    def __iter__(self): # here class behaves as iterable object
        tmp = self.head
        while tmp:
            yield tmp
            tmp = tmp.link

    def insert_at_beginning(self,num): #insert at beginning

        """

        Name : insert_at_beginning()
        Argument : num: int
        Desc: Insertes node with value at beginning
        RType : None

        """

        if self.head == None:
            self.head = Node(num)
            #print("No nodes are preseent")
            return
        temp = Node(num)
        temp.link = self.head
        self.head = temp

    def insert_in_btw(self,num,position):               #insert in between of nodes

        """

        Name : insert_in_btw()
        Argument : num: int, position : int
        Desc: Insertes node with value at specified position
        RType : None

        """

        count = 1
        curr = self.head
        temp = Node(num)

        while count<position-1 and curr!=None:
            curr = curr.link
            count+=1

        if count>1 and curr!=None:
            add_hold = curr.link
            curr.link = temp
            temp.link = add_hold
        else:
            print(f"Cannot Insert at Position : {position}")
            return

    def insert_at_end(self,num):                #insert at end of linked list

        """

        Name : insert_at_end()
        Argument : num: int
        Desc: Insert node with value at end
        RType : None

        """

        if self.head == None:
            self.head = Node(num)
            #print("No nodes are preseent")
            return
        temp = self.head
        while(temp.link!=None):
            temp = temp.link

        temp.link = Node(num)



    def traverseSLL(self):

        """

        Name : traverseSLL()
        Desc : Traversing each node of a linked list
        Rtype : None

        """

        temp = self.head
        while (temp!=None):
            print(temp.value)
            temp = temp.link


    def sort_linkedlist(self):

        """

        Name : sort_linkedlist()
        Desc : Sort Single Linked List using Bubble Sort
        Rtype : None
        Time Complexity : O(n^2)

        """

        if (self.head == None):
            print("Linked List is Empty")

        else:
             current = self.head

             while(current):

                 next_ = current.link

                 while(next_):

                     if (next_.value < current.value):
                         hold = current.value
                         current.value = next_.value
                         next_.value = hold

                     next_ = next_.link

                 current = current.link

             print("Linked List Sorted !")

        return

# This function doesnt belongs to class
# This is User Defined Function
def merge_ll(start,second):

    """
    Name : merge_ll()

    Argument : start : Linked List Object,
               second : Linked List Object
    Desc : Merges second(Linked List) with start(Linked List)
           i.e, start = start + second

    Rtype : None

    """

    tmp = start.head

    while(tmp.link!=None):
        tmp = tmp.link
    tmp.link = second.head


if __name__ == '__main__':

    singleLinkedList = SLinkedList()     # creating LL object (1)
    singleLinkedList_two = SLinkedList() # creating LL object (2)

    #Insertion operations
    # (1)
    singleLinkedList.insert_at_beginning(50)
    singleLinkedList.insert_at_end(60)
    singleLinkedList.insert_at_end(70)
    singleLinkedList.insert_at_end(80)
    singleLinkedList.insert_at_end(60)
    singleLinkedList.insert_at_end(70)
    singleLinkedList.insert_at_end(80)
    singleLinkedList.insert_in_btw(100,3)

    # (2)
    singleLinkedList_two.insert_at_beginning(150)
    singleLinkedList_two.insert_at_end(23)
    singleLinkedList_two.insert_at_end(15)
    singleLinkedList_two.insert_at_end(120)
    singleLinkedList_two.insert_at_end(94)
    singleLinkedList_two.insert_at_end(652)
    singleLinkedList_two.insert_at_end(780)
    singleLinkedList_two.insert_in_btw(87,3)

    merge_ll(singleLinkedList,singleLinkedList_two)     # here singleLinkedList_two is merged with singleLinkedList
                                                        # i.e. singleLinkedList = singleLinkedList + singleLinkedList_two

    singleLinkedList.sort_linkedlist()                  # sort singleLinkedList
    singleLinkedList.traverseSLL()                      # After merging and sorting the resultant linked list will be in Ascending order
