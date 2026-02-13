from functools import total_ordering

@total_ordering
class Node:
    def __init__(self, data, node= None):
        self.data= data
        self.next= node

    def __lt__(self, other):
        if (not isinstance(other, Node)):
            return NotImplemented
        return self.data < other.data
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        
        return self.data==other.data