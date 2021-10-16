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
            yield tmp.value
            tmp = tmp.link
            if tmp == self.head:
                break

    def insert_at_beginning(self,num):  #insert node at beginning of circular linked list

        """
        Name : insert_at_beginning()
        Argument : num: int
        Desc: Insertes node with value at beginning
        RType : None
        """
        
        if self.head == None:
            self.head = Node(num)
            self.head.link = self.head
            return
        else:
            newnode = Node(num)          #create new node instance
            
            last = self.head                
            while(last.link!=self.head): #iterate to last node
                last = last.link
                
            newnode.link = self.head     #link newnode to head node
            self.head = newnode          #assign newnode to head
            last.link = self.head        #link last node to head
            return

    def insert(self,num):

        """
        Name : insert()
        Argument : num: int
        Desc : Appends each value by creating a new node
        Rtype : None
        """
        
        if self.head == None:           # if head is none
            self.head = Node(num)       #create new node for head
            self.head.link = self.head  #point head to itself
            return
        else:
            tmp = self.head             #create head instance
            while(tmp.link!=self.head): #iterate each node unitl reaches head
                tmp = tmp.link
            newnode = Node(num)         #create newnode 
            tmp.link = newnode          #point last node to the newnode inserted
            newnode.link = self.head    #point newnode link to head 
            return

    def insert_at_end(self,num):

        """
        Name : insert_at_end()
        Argument : num: int
        Desc: Insert node with value at end
        RType : None
        """
        
        if self.head == None:
            self.head = Node(num)
            self.head.link = self.head
            return
        else:
            newnode = Node(num)
            tmp = self.head
            while(tmp.link!= self.head):
                tmp = tmp.link
            tmp.link = newnode
            newnode.link = self.head
            return

    def delete_first(self):

        """
        Name : delete_first()
        Argument : None
        Desc: Delete node with value at Beginning of circular linked list
        RType : None
        """

        if self.head == None:
            return "Linked list is empty"
        tmp = self.head
        new = self.head
        
        while(tmp.link!=self.head):
            tmp = tmp.link
            
        new = self.head.link
        self.head = new
        tmp.link = self.head
        return 

    def delete_in_btw(self,position):   #takes argument as position

        """
        Name : delete_in_btw()
        Argument : position : int
        position : position of the node to be deleted
        rtype : None on Success and Failures
        """
        
        if self.head == None:
            print("Circular Linked List in Empty!")
            return
        else:
            count = 1
            curr = self.head
            while count<position-1 and curr.link!=self.head:
                curr = curr.link
                count+=1
                
            if count>1 and count+1==position:
                curr.link = curr.link.link
                return
            print(f"Cannot delete at Position : {position}")
            return

    def delete_end(self):

        """
        Name : delete_end()
        Argument : None
        Desc: Delete node with value at End of circular linked list
        RType : None
        """

        if self.head == None:
            return "Linked list is empty"
        
        tmp = self.head.link
        while(tmp!=self.head):
            adv = tmp.link
            if adv.link == self.head:
                tmp.link = self.head
                return
            else:
                tmp = tmp.link
                
    def search_value_node(self,num):    # search the node (by its value)

        """
        Name : search_value_node()
        Argument : num: int
        Desc: Search for the node which contains data == num
              Iterates from top and bottom simultaneously
        RType : None
        """
        
        temp = self.head
        if temp == None:                # returns if head is empty
            print("Linked List is empty") 
            return
        
        while (temp):                   #iterating each node fromm head
            if temp.value == num:       #returns if the value is found
                print(f"The Node with value : {num},exists!")
                return
            
            temp = temp.link
            
            if (temp == self.head):     #breaks if it reaches head 
                print(f"The Node with value : {num},doesnt exists!")
                return

    def delete_CLL(self):               # delete entire circular linked list

        """
        Name : delete_CLL()
        Desc : Delete Entire Circular Linked List
        Rtype : None
        """
        if self.head == None:       
            print("Circular Linked List is empty, nothin to delete")
            return
        else:
            self.head = None
            print("Circular Linked List Deleted")
            return
    
    def traverseSLL(self):      # Traversing  Circular Linked List

        """
        Name : traverseSLL()
        Desc : Traversing each node s
        Rtype : None
        """
        
        temp = self.head
        while (temp):
            print(temp.value)
            temp = temp.link
            if temp == self.head:
                break
    

singleLinkedList = SLinkedList()  # creating LL object

#Insertion operations

singleLinkedList.insert(70)     # inserting node
singleLinkedList.insert(80)     # inserting node
singleLinkedList.insert(90)     # inserting node
singleLinkedList.insert(100)    # inserting node

singleLinkedList.insert_at_beginning(50) #insert at beginning
singleLinkedList.insert(110)    # inserting node
singleLinkedList.insert(120)    # inserting node

singleLinkedList.insert_at_beginning(150)   #insert at beginning
singleLinkedList.insert_at_end(500) #insert at end
singleLinkedList.insert_at_end(300) #insert at end
#singleLinkedList.traverseSLL()

#Deletion Operation

singleLinkedList.delete_first()     # Delete First
#singleLinkedList.traverseSLL()

singleLinkedList.delete_end()       # Delete End
singleLinkedList.traverseSLL()
print()
#singleLinkedList.search_value_node(80)
singleLinkedList.delete_in_btw(5)               #takes argument as position
print(singleLinkedList.delete_in_btw.__doc__)  #docstring of delete_in_btw
singleLinkedList.traverseSLL()
singleLinkedList.delete_CLL()       # delete entire circular linked list
