# Graph implementation using adjacency list represtentation
#Minor change to test
# A class to represent the adjacency list of the node 
class AdjNode: 
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [None] * self.V 
  
    # Function to add an edge in an undirected graph 
    def addEdge(self, src, dest): 
        # Adding the node to the source node 
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
    # Function to print the graph 
    def printNode(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 
  
if __name__ == "__main__":
    V = 5
    graph = Graph(V)

    graph.addEdge(0, 1) 
    graph.addEdge(0, 4) 
    graph.addEdge(1, 2) 
    graph.addEdge(1, 3) 
    graph.addEdge(1, 4) 
    graph.addEdge(2, 3) 
    graph.addEdge(3, 4) 

    graph.printNode()
