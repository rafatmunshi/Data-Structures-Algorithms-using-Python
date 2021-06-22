class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def addEdge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, src, dest):
        srcleader = self.find(parent, src)
        destleader = self.find(parent, dest)

        if rank[srcleader] < rank[destleader]:
            parent[srcleader] = destleader
        elif rank[srcleader] > rank[destleader]:
            parent[destleader] = srcleader
        else:
            parent[destleader] = srcleader
            rank[srcleader] += 1

    def KruskalsMST(self):
        mst = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        e = 0
        i = 0
        parent = []
        rank = []
        # makeset for disjoint sets
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        while e < self.vertices - 1:
            src, dest, weight = self.graph[i]
            i += 1
            srcparent = self.find(parent, src)
            destparent = self.find(parent, dest)

            if srcparent != destparent:
                e += 1
                mst.append([src, dest, weight])
                self.union(parent, rank, src, dest)

        minCost = 0
        for src, dest, weight in mst:
            minCost += weight
            print('%d to %d with weight %d' % (src, dest, weight))
        print('The total cost for the MST is ', minCost)


graph = Graph(7)
graph.addEdge(0, 1, 1)
graph.addEdge(1, 2, 10)
graph.addEdge(2, 3, 3)
graph.addEdge(0, 5, 2)
graph.addEdge(5, 6, 1)
graph.addEdge(6, 2, 3)
graph.addEdge(3, 4, 1)
graph.addEdge(5, 4, 34)
graph.addEdge(6, 4, 4)

graph.KruskalsMST()