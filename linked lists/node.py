class Node:
    
    def __init__(self, data):
        self.data = data    # can be any type
        self.next = None    # type : Node
        


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
    
    
    
    