from node import Node

class LinkedList:
    def __init__(self, head):
        self.head = head    # type : Node

    # inserts a the new data at the begining of the list
    def insertFirst(self, data = 'd' ):
        n1 = Node(data)
        n1.next = self.head
        self.head = n1
        
        
        
    def insertAtIndex(self, data, index):
        pass

    # ex 1 
    # insert an element 1 place after the end.
    # example-    lst: 1 -> 3 -> 9 
    #             lst.insertOneAfterHead(10)
    #             lst: 1 -> 10 -> 3 -> 9 
    def insertOneAfterHead(self, data): # @TODO
        pass

    # ex 2: 
    # insert an at the end of the list
    # example-    lst: 1 -> 3 -> 9 
    #             lst.insertLast(10)
    #             lst: 1 -> 3 -> 9 -> 10
    def insertLast(self, data): # @TODO
        pass


if __name__ == '__main__':
    n1 = Node(10)
    
    l1 = list(n1)
    
    n2 = Node(5)
    n1.next = n2
    
    ######
    
    l1 = list()
    l1.append(10)
    l1.append(5)
    
    lst = list().append(7)
    
    