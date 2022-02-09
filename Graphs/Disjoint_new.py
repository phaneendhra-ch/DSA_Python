"""

    A disjoint set is to find a minimal spanning tree

    It works for Weighted and Undirected Graph

    Rules :

        1. Connects all vertices together.
        2. No cycle is detected

"""

class Disjoint:

    def __init__(self,vertices):

        self.vertices  = vertices           # taking vertices as a list
        self.parent = {}                    # parent dictionary

        for v in vertices:                  # assign parent of each vertex to itself
            self.parent[v] = v

        self.rank = dict.fromkeys(vertices,0)   # assign rank 0 for each vertex

    def find(self,x):

        #print(f"value of parent[x] = {self.parent[x]} value of x : {x}")

        if (self.parent[x]!=x):
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def Union(self,x,y):

        xset = self.find(x)
        yset = self.find(y)

        print(f"value of xset = {xset}, yset = {yset}")

        if (self.rank[xset] == self.rank[yset]):
            return

        elif (self.rank[xset] < self.rank[yset]):
            self.parent[xset] = yset

        elif (self.rank[xset] > self.rank[yset]):
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset              # either add parent for x -> y or y -> x
            self.rank[xset]+=1

if __name__ == '__main__':

    vertices = ["A","B","C","D","E"]

    dst = Disjoint(vertices)

    dst.Union("A", "B")
    dst.Union("A", "C")
    dst.Union("C", "D")
