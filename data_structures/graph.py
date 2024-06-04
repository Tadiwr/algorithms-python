from lists.linked_list import LinkedList

class Edge:

    def __init__(self, wieight: int, nextVertice) -> None:
        self.weight = -1
        self.nextVertice : Vertice = nextVertice

class Vertice:

    def __init__(self, data = None) -> None:
        self.data = data
        self.edges : set[Edge] = set()


# Graph class

class Graph:

    def __init__(self, rootItem: any = None) -> None:
        self.__vertices : set[Vertice] = set()

    def addVertice(self, data: any):

        newVertice = Vertice(data)
        self.__vertices.add(newVertice)

    def __getVertice(self, target) -> Vertice | None:
        vertices = list(self.__vertices)

        for v in vertices:
            if v.data == target:
                return v
        
        return None

    def addEdge(self, a, b):
        """Connect a and b"""

        verticeA = self.__getVertice(a)
        verticeB = self.__getVertice(b)

        if verticeA and verticeB:
            verticeA.edges.add(Edge(0, verticeB))
            verticeB.edges.add(Edge(0, verticeA))
    
    def getNeighbours(self, vertice: any) -> set:
        outSet = set()
        v = self.__getVertice(vertice)

        if v is not None:
            for e in v.edges:
                outSet.add(e.nextVertice.data)

    def getAllRoutes(self, start: any, end: any, route : LinkedList = LinkedList()):
        rootNode = self.__getVertice(start)

        for edge in rootNode.edges:
            node = edge.nextVertice

            if node.data == end:
                route.insert(end)
                return route
            else:
                route.insert(node.data)
                return self.getAllRoutes(node.data, end, route)



graph = Graph()

graph.addVertice(0)
graph.addVertice(6)
graph.addVertice(7)
graph.addVertice(3)
graph.addVertice(2)
graph.addVertice(1)
graph.addVertice(8)
graph.addVertice(4)
graph.addVertice(5)

graph.addEdge(0, 6)
graph.addEdge(0, 8)
graph.addEdge(0, 4)
graph.addEdge(6, 7)
graph.addEdge(7, 3)
graph.addEdge(3, 2)
graph.addEdge(2, 1)
graph.addEdge(8, 1)
graph.addEdge(4, 5)
graph.addEdge(5, 1)

route = graph.getAllRoutes(0, 1)
route.insertInFront(0)

print(route.printList())