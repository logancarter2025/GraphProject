from Node import *
from Edge import *

class Graph:
    
    '''
    GRAPH REPRESENTATION:
    1)  label_map is a dictionary with key as Node label, value Node object with respective label
    2)  adjacency_map is also dictionary with Node object as key, 
        set of Edges whose start node is the key, as the value
    3)  set of nodes
    4)  set of edges
    
    3 and 4 are not vital to the representation of the graph, but storing these sets into memory
    makes certain operations much faster
    '''
   
    def __init__(self):
        self.label_map = dict()
        self.adjacency_map = dict()
        self.nodes = set()
        self.edges = set()

    #Returns all edges in Graph DONE
    def getAllEdges(self):
        return self.edges
    
    #Populates graph with edges, 
    #if directedFlag = True, then each edge is traversable in both directions
    def fillGraph(self, inputFile, undirectedFlag=False):
        file = open(inputFile)
        for line in file:
            info = line.strip().split(',')
            startNode = Node(info[0])
            endNode = Node(info[1])
            label = float(info[2])
            e = Edge(startNode, endNode, label)
            self.addEdge(e)
            if undirectedFlag:
                e2 = Edge(endNode, startNode, label)
                self.addEdge(e2)
            
    
    def getNodesAlphabetical(self):
        nodes = list(self.getAllNodes())
        nodes.sort()
        return nodes
    
    
    #Returns all edges in Graph with designated startNode DONE
    def getEdgesFromStart(self, startNode):
        s = set()
        if startNode not in self.adjacency_map:
            return s
        return self.adjacency_map[startNode]
    
    #Returns True if there exists and edge with desired startNode, False othewise DONE
    def isEdge(self, startNode):
        return len(self.getEdges(startNode)) != 0
    
    #Returns all edges in Graph with designated startNode and endNode DONE
    def getEdges(self, startNode, endNode):
        s = set()
        if startNode not in self.adjacency_map:
            return s
        for edge in self.adjacency_map[startNode]:
            if edge.getEnd() == endNode:
                s.add(edge)
                
        return s
    
    #Returns True if there exists and edge with desired startNode and endNode, False othewise DONE
    def isEdge(self, startNode, endNode):
        return len(self.getEdges(startNode, endNode)) != 0
    
    #Returns True if there exists and edge with desired startNode, endNode, and label, False othewise DONE
    def isEdge(self, startNode, endNode, label):
        if startNode not in self.adjacency_map:
            return False
        
        e = Edge(startNode, endNode, label)
        return e in self.adjacency_map[startNode]
        
    #Returns all Nodes in Graph DONE
    def getAllNodes(self):
        return self.nodes
    
    #Returns True if the Node is found in the graph, false otherwise DONE
    def isNode(self, node):
        if not isinstance(node, Node):
            return node in self.label_map
        return node in self.adjacency_map
    
    #adds node into graph if not already present
    def addNode(self, node):
        if self.isNode(node):
            return
        
        if isinstance(node, Node):
            self.adjacency_map[node] = set()
            self.label_map[node.getLabel()] = node
            self.nodes.add(node)
            
        else:
            n = Node(node)
            self.label_map[node] = n
            self.adjacency_map[n] = set()
            self.nodes.add(n)
    
    #Adds the edge into the graph if not already present
    def addEdge(self, edge):
        if not isinstance(edge, Edge):
            return
        if self.isEdge(edge.getStartNode(), edge.getEndNode(), edge.getLabel()):
            return
        self.addNode(edge.getStartNode())
        self.addNode(edge.getEndNode())
        self.adjacency_map[edge.getStartNode()].add(edge)
        
        self.edges.add(edge)