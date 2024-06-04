
class Edge:

    def __init__(self, wieight: int, nextNode) -> None:
        self.weight = -1
        self.nextNode : Node = nextNode

class Node:

    def __init__(self, data = None) -> None:
        self.data = data
        self.edges : set[Edge] = set()


def addEdge(data, weighting: int) -> Edge:
    """creates a new edge object with a 
    weighting and next node"""

    newNode = Node(data)
    newEdge = Edge(weighting, newNode)

    return newEdge

def neighbours(node : Node) -> set:
    finalSet : set[Node] = set()

    for e in node.edges:
        finalSet.add(e.nextNode.data)
        
    return finalSet

rootNode  = Node(0)

rootNode.edges.add(addEdge(6, 0))
rootNode.edges.add(addEdge(8, 0))
rootNode.edges.add(addEdge(4, 0))

def search(rootNode: Node, target: any) -> Node:

    edges = list(rootNode.edges)

    if rootNode.data == target:
        return rootNode

    for edge in edges:

        if edge.nextNode.data == target:
            return edge.nextNode
        else:
            for x in edge.nextNode.edges:
                return search(x.nextNode, target)
            
    return None

def addEdgeTo(targetNode: any, newData: any) -> bool:

    pNode = search(rootNode, targetNode)
    cNode = search(rootNode, newData)

    # If node we want to add to pNode already exists
    # make it point to that
    if cNode is not None and pNode is not None:
        newEdge = Edge(0, cNode)
        pNode.edges.add(newEdge)
        return True

    # Else make a new item 
    if pNode is not None:
        pNode.edges.add(addEdge(newData, 0))
        return True
    
    return False


addEdgeTo(6, 7)
addEdgeTo(3, 1)
addEdgeTo(7, 3)
addEdgeTo(7, 2)
addEdgeTo(2, 3)

def printGraph(root: Node):

    for items in list(root.edges):
        print(f"{items.nextNode.data} -> {list(neighbours(items.nextNode))}")
        printGraph(items.nextNode)

print(printGraph(rootNode))