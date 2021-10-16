class Node :
    def __init__(self,value =None):
        self.value = value
        self.left = None
        self.right = None

class SLinkedList:
    
    def __init__(self): # constructor for the class
        self.head = self.behead = None  #adding another item for traversal reverse
        
    def __iter__(self): # here class behaves as iterable object
        tmp = self.head
        while tmp:
            yield tmp
            tmp = tmp.right
            
    def insert_at_beginning(self,num):  #insert node at beginning of linked list

        """
        Name : insert_at_beginning()
        Argument : num: int
        Desc: Insertes node with value at beginning
        RType : None
        """

        if self.head == None:
            self.head = Node(num)
            self.behead = self.head
            return
                
        newnode = Node(num)             #creating new node instance
        newnode.right = self.head       #point newnode right to head
        self.head = newnode             #assign new node to head
        self.head.right.left = newnode  #assign head of right.left to newnode
        return


    def insert(self,num):           #insert node to a double linked list
        
        """
        Name : insert()
        Argument : num: int
        Desc : Appends each value by creating a new node
        Rtype : None
        """
        
        if self.head == None:                       # if head is none
            self.head  = self.behead =  Node(num)   #create a new head node
            return
        else:
            tmp = self.head         # creating a new head instance
            while(tmp.right!=None): #iterate unitl next node is None
                tmp = tmp.right
                
            newnode = Node(num)     #creating new node instance
            newnode.left = tmp      #appending left of new node to previous node
            tmp.right = newnode     #appending new node to the last node
            self.behead = newnode   #assigning latest node to bottom node
            return

    def insert_at_bw(self,position,num):

        """
        Name : insert_at_bw()
        Argument : position: int, num: int
        Desc: Insert node with value at specific location
              If position > len(DLL) --> Insert at End
              If position < 1 --> Terminate
              If position > 1 and position < len(DLL) --> Perform Insertion
        RType : None
        """
        if (position < 1):
            print(f"Cannot insert num : {num} at position : {position} ")
            return
        
        if (position>len([each for each in singleLinkedList])):
            print("Node Inserted at End!")
            self.insert_at_end(num)
            return
        
        if self.head == None:
            print("Double Linked List is Empty")
            return
        else:
            count = 1
            curr_r = self.head
            newnode = Node(num)
            while count<position-1 and curr_r!=None:
                count+=1
                curr_r = curr_r.right
            
            if count>1 and curr_r!=None:
                    
                var = curr_r.right
                curr_r.right = newnode
                newnode.left = var.left
                newnode.right = var
                var.left  = newnode 
                return
            else:
                print(f"Cannot insert num : {num} at position : {position} ")
                return
            
    def insert_at_end(self,num):
        
        """
        Name : insert_at_end()
        Argument : num: int
        Desc: Insert node with value at end
        RType : None
        """
        
        if self.head == None:
            self.head  = self.behead =  Node(num)
            return
        else:
            newnode = Node(num)             #create a newnode instance
            newnode.left = self.behead      #assign newnode left to behead
            self.behead.right = newnode     #assign behead right to newnode
            self.behead = newnode           #assign newnode to behead
            return 

    def delete_start(self):                 #delete starting node of circular LL

        """
        Name : delete_start()
        Argument : None
        Desc: Delete node with value at Beginning
        RType : None
        """
        
        if self.head == None:               #if head is none throw error
            print("Double Linked List is empty")
            return
        else:
            tmp = self.head.right
            self.head = tmp
            self.head.left = None
            return

    def delete_node_bw(self,position):

        """
        Name : delete_node_bw()
        Argument : position : int
        Desc: Delete node at specific position on success, else, return
        RType : None
        """

        if self.head == None or self.behead==None:
            print("Double Linked List is empty")
            return
        else:
            count = 1
            curr_r =  self.head
            while count<position-1 and curr_r!=None:
                count+=1
                curr_r = curr_r.right

            if count>1 and curr_r!=None:
                var = curr_r.right.right
                var.left = curr_r
                curr_r.right = var
                return
            else:
                print(f"Cannot delete at Position : {position}")
                return
                
        
    def delete_end(self):                   #delete ending node of circular LL
        
        """
        Name : delete_end()
        Argument : None
        Desc: Delete node with value at End
        RType : None
        """
        
        if self.head == None or self.behead == None:    #if head or tail is none throw error
            print("Double Linked List is empty")
            return
        else:
            tmp = self.behead.left                  # assign behead left instance to tmp 
            tmp.right = None                        # assign tmp right to None
            self.behead = tmp                       # assign tmp to behead
            return
        
    def search_value_node(self,num): # search the node (by its value)
        
        """
        Name : search_value_node()
        Argument : num: int
        Desc: Search for the node which contains data == num
              Iterates from top and bottom simultaneously
        RType : None
        """
        
        temp_top = self.head
        temp_bottom = self.behead
        
        if temp_top == None or temp_bottom == None:  # returns if head is empty
            print("Linked List is empty") 
            return
        while temp_top != None and temp_bottom != None:
            if temp_top.value == num or temp_bottom.value == num:
                print(f"The Node with value : {num},exists!")
                return
            temp_top = temp_top.right
            temp_bottom = temp_bottom.left
        print(f"The Node with value : {num},doesnt exists!")
        return

    def delete_DLL(self):

        """
        Name : delete_DLL()
        Desc : Delete Entire Double Linked List
        Rtype : None
        """
        
        tmp = self.head
        if tmp == None:
            print("Linked List is empty nothing to delete")
            return

        while tmp:
            tmp.left = None
            tmp = tmp.right
        self.head = None
        self.behead = None
        print("Double Linked List Deleted")
        return
            
    
    def traverseSLL_top(self):      # Traversing from Top node
        """
        Name : traverseSLL_top()
        Desc : Traversing each node from top (right)
        Rtype : None
        """
        temp = self.head
        while (temp!=None):
            print(temp.value)
            temp = temp.right
            
    def traverseSLL_bottom(self):   # Traversing from Bottom node
        
        """
        Name : traverseSLL_bottom()
        Desc : Traversing each node from bottom (left)
        Rtype : None
        """
        
        temp = self.behead
        while (temp!=None):
            print(temp.value)
            temp = temp.left
    
singleLinkedList = SLinkedList()            # creating LL object

#Insertion Operations

singleLinkedList.insert(10)
singleLinkedList.insert(20)
singleLinkedList.insert(30)
singleLinkedList.insert(60)

#singleLinkedList.traverseSLL_top()         #calling top traversal func
#singleLinkedList.traverseSLL_bottom()      #calling bottom traversal func

#searching a node with value
#singleLinkedList.search_value_node(60)      #searching value for a node

singleLinkedList.insert_at_beginning(100)   #inserting node at beginning
singleLinkedList.insert_at_beginning(200)   #inserting node at beginning
singleLinkedList.traverseSLL_top()

#singleLinkedList.insert_at_end(23)          #insert node at end
#singleLinkedList.insert_at_end(55)          #insert node at end
#singleLinkedList.traverseSLL_top()
print()
singleLinkedList.delete_start()             #delete starting node
singleLinkedList.traverseSLL_top()
print()
singleLinkedList.traverseSLL_bottom()
print()
"""
print()
singleLinkedList.delete_end()               #delete end node
singleLinkedList.traverseSLL_top()
print()
singleLinkedList.traverseSLL_bottom()
print()
"""
singleLinkedList.insert_at_bw(3,500)        #delete node at position 3
singleLinkedList.traverseSLL_top()
print()
singleLinkedList.traverseSLL_bottom()
singleLinkedList.delete_DLL()               #delete entire double linked list
