"""

    A disjoint set is to find a minimal spanning tree

    It works for Weighted and Undirected Graph

    Rules :

        1. Connects all vertices together.
        2. No cycle is detected

"""

class Disjoint:

    def __init__ (self,n):

        self.rank = [0]*n                   # each node has a initial rank 0
        self.parent = [i for i in range(n)] # each vertex is parent to itself


    def find(self,x):

        """

        Name: find()
        Arguments : x : Vertex of the graph
        Desp : Here it will check the parent for the given vertex
        RType: None

        """

        print(f"value of parent[x] = {self.parent[x]} value of x : {x}")

        if (self.parent[x]!= x):
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # Do union of two sets represented by x and y.
    def Union(self,x,y):

        #Find current sets of x and y

        xset = self.find(x)
        yset = self.find(y)

        print(f"value of xset = {xset}, yset = {yset}")

        # If they are already in same set
        if (xset == yset):
            return

        # Put smaller ranked item under bigger ranked item if ranks are different
        if (self.rank[xset] < self.rank[yset]):
            self.parent[xset] = yset

        elif (self.rank[xset] > self.rank[yset]):
            self.parent[yset] = xset

        else:                                   # if both are at same rank

            self.parent[yset] = xset              # either add parent for x -> y or y -> x
            self.rank[xset]+=1

#Driver Code
if __name__ == '__main__':

    dst = Disjoint(5)

    dst.Union(0, 2)
    dst.Union(4, 2)
    dst.Union(3, 1)

    if dst.find(4) == dst.find(0):
    	print('Yes')
    else:
    	print('No')
