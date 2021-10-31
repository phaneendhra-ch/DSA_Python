"""

Single Source Shortest Path(SSSP) using BFS in Python

    Aim of SSSP :
    We can find the minimum distance from source Vertex to destination vertex with minimum distance

Author : Phaneendhra

"""
class Graph:
    def __init__(self, gdict=None):

        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def bfs(self, start, end):

        queue = []              # create empty queue
        queue.append([start])   # append list [start] to queue

        while queue:
            path = queue.pop(0)     # pop first list from queue
            #print(path,sep = "\n")
            node = path[-1]         # get last value from popped list

            if node == end:         # if last val == destination node then return path
                return path

            for adjacent in self.gdict.get(node, []):       # iterate through each adjacent vetex of node

                new_path = list(path)                       # get nested path
                new_path.append(adjacent)                   # append path to new_path
                #print(adjacent,new_path,sep = " ")

                queue.append(new_path)                      # append new path to queue
                #print(queue)

customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g = Graph(customDict)
print(g.bfs("a", "f"))
