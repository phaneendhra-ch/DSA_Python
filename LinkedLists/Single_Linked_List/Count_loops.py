class Node:

    def __init__(self,value=None):          #constructor class
        self.value = value
        self.link = None

class LinkedList :

    def __init__(self):                     #constructor
        self.head = None

    def insert(self,num):                   #insert function

        """
        Name: insert()
        Arguments : num:int
        Desp : Appends each node to the previous node through link
        RType: None
        """

        if self.head == None:               #if head is None
            self.head = Node(num)
            return
        else:
            tmp = self.head
            while(tmp.link!=None):
                tmp = tmp.link

            tmp.link = Node(num)
            return tmp.link

    def detectloop(self):

        """

        Name : detectloop()
        Desp : Dsiplay the values and length of the nodes in connected through loop
        RType: None

        """

        li = []
        tmp = self.head
        while(tmp):
            li.append(tmp)
            tmp = tmp.link
            if tmp in li:
                #if loop detected then print length of loop and display nodes in loop
                print(f"Loop detected and length of the loop is {len(li[li.index(tmp):])} -> {list(map(lambda li:li.value,li[li.index(tmp):]))}")
                return
        return

    def display(self):

        """
        Name : display()
        Desc : Traversing each node
        Rtype : None
        """

        if self.head == None:
            print("Linked List is empty")
            return

        tmp = self.head
        while (tmp!=None):
            print(tmp.value)
            tmp = tmp.link
        return

if __name__ == '__main__':

    my_linked_list = LinkedList()
    a = my_linked_list.insert(1)
    b = my_linked_list.insert(2)
    c = my_linked_list.insert(3)
    d = my_linked_list.insert(4)
    e = my_linked_list.insert(5)
    my_linked_list.insert(6).link  = b.link        # Here node(6) is linked towards node(2).link
    #my_linked_list.display()
    my_linked_list.detectloop()                    # detectloop function
