# create a set- spset- initially empty, add all the vertices whose shortest paths are already calculated
# distance[]- initially infinite for all the vertices, 0 for the source vertex
# loop- until spset doesnt contain all the vertices
# pick a vertex which is not in the spset which has min distance value from source
# include in the spset
# update distances for all the adj of this vertex
import sys
class Graph:
    def __init__(self, vertices):
        self.vertices= vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printShortestPath(self, distance):
        for vertex in range(self.vertices):
            print(vertex, ' distance from source- ', distance[vertex])

    def minDistance(self, distance, spset):
        min = sys.maxsize
        for vertex in range(self.vertices):
            if distance[vertex] < min and spset[vertex] == False:
                min = distance[vertex]
                indexofshortestDistanceVertex = vertex
        return indexofshortestDistanceVertex


    def dijkstra(self, src):
        distance = [sys.maxsize]*self.vertices
        distance[src]=0
        spset = [False]*self.vertices

        for vertex in range(self.vertices):
            u = self.minDistance(distance, spset)
            spset[u]= True
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and spset[v] == False and distance[v] > distance[u] + self.graph[u][v]:
                    distance[v] = distance [u] + self.graph[u][v]

        self.printShortestPath(distance)

g= Graph(10)
g.graph=[[0, 85, 217, 0, 173, 0, 0, 0, 0, 0],
         [85, 0, 0, 0, 0, 80, 0, 0, 0, 0],
         [217, 0, 0, 0, 0, 0, 186, 103, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 183, 0, 0],
         [173, 0, 0, 0, 0, 0, 0, 0, 0, 502],
         [0, 80, 0, 0, 0, 0, 0, 0, 250, 0],
         [186, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 103, 183, 0, 0, 0, 0, 0, 167],
         [0, 0, 0, 0, 0, 250, 0, 0, 0, 84],
         [0, 0, 0, 0, 502, 0, 0, 167, 84, 0]]
g.dijkstra(0)