"""

Graph Data Structure in Python

Author : Phaneendhra

"""
class Graph:

    def __init__(self):
        self.gdict = dict()

    def addedge(self,vertex,edge):

        """

        Name : addedge()
        Arguments : vertex : vertex of the graph
                    edge : vetex connected through edges of the graph
        Desp : Creates a graph by connecting to vertices through edges
        Rtype: None

        """

        if vertex not in self.gdict:
            self.gdict[vertex] = list()

        if type(edge) == list:
            for each in edge:
                self.gdict[vertex].append(each)
        else:
            self.gdict[vertex].append(edge)
        return

    def BFS(self,vertex):

        """

        Breadth First Search in Python uses 'Queue' Data Structure

        Name : BFS()
        Arguments : vertex : vertex of the graph
        Desp  : Traverse through graph by keep tracking of visited and unvisited vertex
        Rtype : None

        Total Time Complexity : O(V+E)

        """

        visited = [vertex]                                      # keeps track of all visisted nodes
        queue = [vertex]                                        # queue data Structure

        while queue:                                            # -> Time Complexity : O(V), V: Vertex
            new_vertex = queue.pop(0)                           # pop first element from queue
            print(new_vertex,end=" ")
            for adjacentvertex in self.gdict[new_vertex]:       # iterate through all neighbouring nodes of new_vertex
                                                                    # Time completely : O(E), E : Edge
                if adjacentvertex not in visited:               # if adjacentvertex is not visited then append to visited (list)
                    visited.append(adjacentvertex)
                    queue.append(adjacentvertex)                # append adjacentvertex to queue

                                                                # Total Time Complexity : O(V+E)
    def DFS(self,vertex):

        """

        Depth First Search in Python uses 'Stack' Data Structure

        Name : DFS()
        Arguments : vertex : vertex of the graph
        Desp  : Traverse through graph by keep tracking of visited and unvisited vertex
        Rtype : None

        Total Time Complexity : O(V+E)
        
        """

        visited  = [vertex]                                    # keeps track of all visisted nodes
        stack = [vertex]                                       # stack data structure

        while stack:                                           # -> Time Complexity : O(V), V: Vertex

            new_vertex = stack.pop()                           # pop last element from the list
            print(new_vertex,end=" ")                          # popped out element
            for adjacentvertex in self.gdict[new_vertex]:      # iterate through all neighbouring nodes of new_vertex
                                                                    # Time completely : O(E), E : Edge
                if adjacentvertex not in visited:              # if adjacentvertex is not visited then append to visited (list)
                    visited.append(adjacentvertex)
                    stack.append(adjacentvertex)               # append adjacentvertex to stack

                                                               # Total Time Complexity : O(V+E)
if __name__ == '__main__':

    sample_graph = Graph()
    sample_graph.addedge('A','B')
    sample_graph.addedge('A','C')
    sample_graph.addedge('B',['A','C'])
    sample_graph.addedge('C','A')
    sample_graph.BFS('A')
    sample_graph.DFS('A')
    print(f"\nGraph -> {sample_graph.gdict}")
