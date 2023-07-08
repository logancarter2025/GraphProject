class Node:
    def __init__(self, label=None):
        self.label = label
        
    def getLabel(self):
        return self.label
    
    def __lt__(self, other):
        return self.label < other.getLabel()
    
    def __hash__(self):
        return hash(self.label)
    
    def setLabel(self, label):
        self.label = label
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.label == other.getLabel()
    
    def __str__(self):
        s = 'Node ('
        s += str(self.label)
        s += ')'   
        
        return s