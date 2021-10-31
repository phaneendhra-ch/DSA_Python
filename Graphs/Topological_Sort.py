"""

Topological Sorting in Python

    Topological order can be one of the subsets of all the permutations of all the vertices
    following the condition that for every directed edge x → y,
    x will come before y in the ordering.

Time Complexity : O(V+E)

Author : Phaneendhra

"""

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)                                          # graph using default dict

    def addedge(self,vertex,edge):
        self.graph[vertex].append(edge)                                         # add node to the vertex

    def topologicalSortUtil(self,v,visited,stack):

        visited.append(v)                                                       # mark the node as visisted

        for i in self.graph[v]:                                                 # iterate through adjacent nodes of v
            if i not in visited:                                                # check if adjacent nodes are not in visited
                self.topologicalSortUtil(i, visited, stack)                     # if not visited call the fucntion recursively w.r.t node i (here i is our adjacent node of v)

        stack.append(v)                                                         # append the node to stack

    def topologicalsort(self):

        visited, stack = [],[]                                                  # visited list and stack list

        for k in list(self.graph):                                              # convert all keys into list and iterate through it
            if k not in visited:                                                # if vertex is not visited call topologicalSortUtil with current vertex k
                self.topologicalSortUtil(k, visited, stack)

        print(stack[::-1])                                                      # print stack in reverse order


if __name__ == '__main__':

    sample_graph = Graph()                                                      # create graph instance

    sample_graph.addedge("A", "C")                                              # addedge function
    sample_graph.addedge("C", "E")
    sample_graph.addedge("E", "H")
    sample_graph.addedge("E", "F")
    sample_graph.addedge("F", "G")
    sample_graph.addedge("B", "D")
    sample_graph.addedge("B", "C")
    sample_graph.addedge("D", "F")

    sample_graph.topologicalsort()                                              # topologicalsort function
