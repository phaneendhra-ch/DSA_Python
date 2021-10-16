"""
Creating Stack Using List
Author : Phaneendhra
"""

class StackList:

    def __init__(self):         # constructor for my class
        self.stacklist = []

    def __repr__(self):

        values = list(map(str,self.stacklist[::-1]))
        return " ".join(values)

    def push(self,num:int):     # push operations

        self.stacklist.append(num)
        print(f"{num} pushed into stack !")
        return

    def pop(self):              # pop operations

        if self.stacklist != []:
            print(f"{self.stacklist[-1]} has been removed from stack !")
            self.stacklist.pop()
        else:
            print("Stack is Empty, Cannot perform pop operation !")
        return


    def peek(self):             # peek operations

        if self.stacklist != []:
            print(f"{self.stacklist[-1]} it current top stack !")
        else:
            print("Stack is Empty!")
        return


    def isEmpty(self):          # isEmpty Functions

        if self.stacklist != []:
            print("False")
        else:
            print("True")
        return

if __name__ == "__main__":

    mystack = StackList()
    mystack.push(1)     #push item
    mystack.push(2)     #push item
    mystack.push(3)     #push item
    mystack.peek()      #peek stack
    mystack.isEmpty()   #Check is stack Empty or not
    mystack.pop()       #pop item
    print(mystack)
