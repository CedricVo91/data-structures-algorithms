class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}

    def addVertex(self, node):  ###correct as in Solutions
        self.number_of_nodes += 1
        self.adjacentList[node] = []

    def addEdge(self, node1, node2):
        # edge already added, don't repeat yourself
        if node2 in self.adjacentList[node1] or node1 in self.adjacentList[node2]:
            return

        self.adjacentList[node1].append(
            node2
        )  # I do not want to replace the empty array but fill it up
        self.adjacentList[node2].append(
            node1
        )  # not scalable if I want to add many nodes at once...


graph1 = Graph()

graph1.addVertex(0)
graph1.addVertex(1)
graph1.addVertex(2)

graph1.addEdge(0, 1)
graph1.addEdge(0, 2)
graph1.addEdge(0, 2)

print(graph1.adjacentList)

print(graph1.number_of_nodes)
