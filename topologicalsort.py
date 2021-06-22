# from collections import defaultdict
# class Graph:
#     def __init__(self, vertices):
#         self.graph = defaultdict(list)
#         self.vertices = vertices
#
#     def addEdge(self, u, v):
#         self.graph[u].append(v)


def topological_sort(graph):
    indegrees = {node: 0 for node in graph}

    for node in graph:
        for adj in graph[node]:
            indegrees[adj] += 1

    nodesWithNoIncomingEdges = []
    for node in graph:
        if indegrees[node] == 0:
            nodesWithNoIncomingEdges.append(node)

    topologicalSortedOrder = []
    while len(nodesWithNoIncomingEdges) > 0:
        node = nodesWithNoIncomingEdges.pop()
        topologicalSortedOrder.append(node)
        for adj in graph[node]:
            indegrees[adj] -= 1
            if indegrees[adj] == 0:
                nodesWithNoIncomingEdges.append(adj)

    if len(topologicalSortedOrder) == len(graph):
        return topologicalSortedOrder
    else:
        raise Exception("This graph has a cycle! Topological sort is not possible")


g = {0: [1, 3], 1: [2], 2: [6], 3: [4, 5, 8], 4: [7, 8], 5: [6], 6: [7], 7: [], 8: []}
# g = Graph(9)
# g.addEdge(0, 1)
# g.addEdge(1, 2)
# g.addEdge(0, 3)
# g.addEdge(2, 6)
# g.addEdge(3, 4)
# g.addEdge(3, 5)
# g.addEdge(3, 8)
# g.addEdge(4, 7)
# g.addEdge(4, 8)
# g.addEdge(5, 6)
# g.addEdge(6, 7)

print(topological_sort(g))
