class Edge:
    def __init__(self, startNode, endNode, label=None):
        self.start = startNode
        self.end = endNode
        self.label = label
        
    def getLabel(self):
        return self.label
    
    def __hash__(self):
        return hash(self.start) + 2*hash(self.end) + 3*hash(self.label)
    
    def setLabel(self, label):
        self.label = label
    
    def getStartNode(self):
        return self.start
    
    def getEndNode(self):
        return self.end
    
    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return self.label == other.getLabel() and self.start == other.getStart() and self.end == other.getEnd()
    
    def __str__(self):
        s = str(self.start)
        s += " -> "
        s += str(self.end)
        s += ": "
        s += str(self.label)   
        
        return s