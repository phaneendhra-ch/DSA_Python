"""
Creating Stack Using List with Limited Size
Author : Phaneendhra
"""

class StackList:

    def __init__(self,Size:int):                        # constructor for my class
        self.stacklist = []
        self.Size = Size

    def __repr__(self):

        values = list(map(str,self.stacklist[::-1]))    #reversing the list and convertin each list item to string
        return " ".join(values)                         #each item is seperated by a space

    def push(self,num:int):                             # push operations

        if len(self.stacklist) == self.Size:
            print("StackOverFlow !!")
            return

        self.stacklist.append(num)
        print(f"{num} pushed into stack !")
        return

    def pop(self):                                      # pop operations

        if self.stacklist != []:
            print(f"{self.stacklist[-1]} has been removed from stack !")
            self.stacklist.pop()
        else:
            print("Stack is Empty, Cannot perform pop operation !")
        return


    def peek(self):                                     # peek operations

        if self.stacklist != []:
            print(f"{self.stacklist[-1]} it current top stack !")
        else:
            print("Stack is Empty!")
        return


    def isEmpty(self):                                  # isEmpty Functions

        if self.stacklist != []:
            print("False")
        else:
            print("True")
        return


if __name__ == "__main__":

    mystack = StackList(5)
    mystack.push(1)     #push item
    mystack.push(2)     #push item
    mystack.push(3)     #push item
    mystack.peek()      #peek stack
    mystack.isEmpty()   #Check is stacBk Empty or not
    mystack.pop()       #pop item
    mystack.push(8)     #push item
    mystack.push(9)     #push item
    mystack.push(10)    #push item
    print(mystack)      #print stack
