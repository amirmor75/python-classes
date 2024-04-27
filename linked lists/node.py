class Node:
    
    def __init__(self, data):
        self.data = data    # can be any type
        self.next = None    # type : Node
        
class LinkedList:
    def __init__(self, head):
        self.head = head    # type : Node
    
    # inserts a the new data at the begining of the list
    def insertAtBegin(self, data = 'd' ):
        n1 = Node(data)
        n1.next = self.head
        self.head = n1
        
        
        
    def insertAtIndex(self, data, index):
    
        

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
    
    
    
    