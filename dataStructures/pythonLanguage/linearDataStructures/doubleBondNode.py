from functools import total_ordering

from node import Node

@total_ordering
class DoubleBondNode(Node):
    prev= None

    def __init__(self, data, prev, next):
        super().__init__(data, node= next)
        self.prev= prev

    def __lt__(self, other):
        if (not isinstance(other, DoubleBondNode)):
            return NotImplemented
        return self.data < other.data
    
    def __eq__(self, other):
        if not isinstance(other, DoubleBondNode):
            return False
        
        return self.data==other.data