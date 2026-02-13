from node import Node

class Stack:
    __top= None

    def __init__(self):
        pass

    def push(self, data):
        newNode= Node(data)
        newNode.next= self.__top
        self.__top= newNode
    
    def pop(self):
        if self.isEmpty():
            return None
        
        data= self.__top.data
        self.__top= self.__top.next

        return data
    
    def top(self):
        if self.isEmpty():
            return None
        return self.__top.data

    def isEmpty(self)->bool:
        return not self.__top