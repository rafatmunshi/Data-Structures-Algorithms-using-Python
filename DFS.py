from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtility(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for adj in self.graph[vertex]:
            if adj not in visited:
                self.DFSUtility(adj, visited)

    def DFS(self, vertex):
        visited = set()
        self.DFSUtility(vertex, visited)


graph= Graph()
graph.addEdge(1,2)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.addEdge(1,5)
graph.addEdge(5,6)
graph.addEdge(6,7)
graph.addEdge(5,8)
graph.addEdge(1,9)
graph.addEdge(9,10)

graph.DFS(2)