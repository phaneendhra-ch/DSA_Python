"""
Case : Find out minimum value in Stack using O(1) Complexity.
Author : Phaneendhra

Note : Do not insert duplicate values
"""

class StackList:

    def __init__(self):
        self.stacklist = []
        self.minimum = []

    def __repr__(self):

        if self.stacklist != []:
            values = list(map(str,self.stacklist[::-1]))
            return " ".join(values)
        else:
            return ""

    def push(self,num):

        if self.stacklist == []:
            self.minimum.append(num)
            self.stacklist.append(num)
        else:
            if num in self.stacklist:
                print("Cannot insert duplicate values")
                return
            if (num < self.minimum[-1]):
                self.minimum.append(num)
            self.stacklist.append(num)

        print(f"{num} has been inserted into stack successfully !")
        return

    def pop(self):

        if self.stacklist == []:
            print("Stack is Empty, cannot perform pop operation")
        else:
            if self.stacklist[-1] == self.minimum[-1]:
                self.minimum.pop()
                if self.minimum == []:
                    self.minimum = [None]

            print(f"{self.stacklist[-1]} has been popped out !")
            self.stacklist.pop()
        return

if __name__ == "__main__":
    mystack = StackList()
    mystack.push(5)
    mystack.push(2)
    mystack.push(4)
    mystack.push(1)
    mystack.push(6)
    mystack.push(0)

    print(mystack.minimum[-1])
    print(mystack)

    mystack.pop()
    print(mystack.minimum[-1])
    print(mystack)
