from node import Node

class SimpleLinkList:
    __size= 0
    __head= None

    def __init__(self):
        pass

    def add(self, data):
        newNode= Node(data= data)
        if not self.__head:
            self.__head= newNode
            self.__size= 1;
            return

        node= self.__head
        
        while(node.next):
            node= node.next
        
        node.next= newNode
        self.__size+=1
    
    def size(self)->int:
        return self.__size

    def reverse(self):
        nodeAux= self.__head
        node= None
        while nodeAux:
            node= Node(nodeAux.data, node)
            nodeAux= nodeAux.next
        self.__head= node
    
    def insert(self, data, index)->bool:
        if index>self.__size or index<0:
            return False
        
        if index==0:
            self.__head= Node(data, self.__head)
            self.__size+=1
            return True
        
        current= self.__head
        for _ in range(index-1):
            current= current.next

        current.next= Node(data, current.next)
        self.__size+=1

        return True
    
    def __iter__(self):
        current= self.__head
        while current:
            yield current.data
            current= current.next
    
    def __str__(self):
        res= "["
        current= self.__head
        while current:
            res= res + f"{current.data}"
            if current.next:
                res= res+ ', '
            current=current.next
        return res+"]"
    

