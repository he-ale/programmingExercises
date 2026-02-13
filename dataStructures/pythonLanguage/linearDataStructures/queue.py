from node import Node

class Queue:
    __first= None
    __last= None

    def __init__(self):
        pass

    def enqueue(self, data):
        newNode= Node(data)
        if not self.__first:
            self.__first= self.__last= newNode
            return 
        self.__last.next= newNode
        self.__last= newNode

    def isEmpty(self)->bool:
        return self.__first is None
    
    def dequeue(self):
        if self.isEmpty():
            return None
        
        data= self.__first.data
        self.__first= self.__first.next

        if(self.__first):
            self.__last= None

        return data
    
    def last(self):
        if self.isEmpty():
            return None
        return self.__last.data
    
    def first(self):
        if self.isEmpty():
            return None
        return self.__first.data
