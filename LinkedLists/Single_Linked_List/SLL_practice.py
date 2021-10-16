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
        if self.head == None:
            self.head = Node(num)         
            #print("No nodes are preseent")
            return
        temp = Node(num)
        temp.link = self.head
        self.head = temp

    def insert_in_btw(self,num,position): #insert in between of nodes
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
        
    def insert_at_end(self,num): #insert at end of linked list
        if self.head == None:
            self.head = Node(num) 
            #print("No nodes are preseent")
            return
        temp = self.head
        while(temp.link!=None):
            temp = temp.link
                
        temp.link = Node(num)

    def delete_head(self):  # delete node at beginning
        a = self.head
        if a == None:
            print("Linked List doesnt exists")
            return
        self.head = a.link
        return

    def delete_in_btw(self,position):

        count = 1
        curr = self.head

        if count+1 == position: #delete immediate head node
            self.head.link = self.head.link.link
            return
        while count<position-1 and curr!=None:  #delete intermediate node
            curr = curr.link
            count+=1
        try :
            if count >1 and curr!=None:
                curr.link  = curr.link.link
                return
            else:
                print(f"Cannot delete at Position : {position}")
                return
        except:
            print(f"Cannot delete at Position : {position}")
            return
            
    def delete_end(self):   # delete node at end
        tmp = self.head
        if tmp == None:
            print("Linked List doesnt exists")
            return
        
        while tmp!= None:
            b = tmp.link
            if (b.link == None):
                tmp.link = None
                return
            tmp = tmp.link
        return

    def search_value_node(self,num): # search the node (by its value)
        
        temp = self.head
        if temp == None:        # returns if head is empty
            print("Linked List is empty") 
            return
        while temp != None:
            if temp.value == num:
                print(f"The Node with value : {num},exists!")
                return
            temp = temp.link
        print(f"The Node with value : {num},doesnt exists!")
        return

    def delete_SLL(self):

        if self.head == None:
            print("Linked List is empty, nothing to delete")
            return
        else:
            self.head = None
            
    def traverseSLL(self):
        temp = self.head
        while (temp!=None):
            print(temp.value)
            temp = temp.link
    

singleLinkedList = SLinkedList()  # creating LL object

#Insertion operations
singleLinkedList.insert_at_beginning(50)
singleLinkedList.insert_at_end(60)
singleLinkedList.insert_at_end(70)
singleLinkedList.insert_at_end(80)
singleLinkedList.insert_in_btw(100,3)

singleLinkedList.traverseSLL()

#singleLinkedList.search_value_node(80)

#Deletion operations
#singleLinkedList.delete_head()
#singleLinkedList.traverseSLL()
#singleLinkedList.delete_end()
#singleLinkedList.traverseSLL()
singleLinkedList.delete_in_btw(2)

singleLinkedList.traverseSLL()
singleLinkedList.delete_SLL()       # delete eniter single linked list
singleLinkedList.traverseSLL()      
