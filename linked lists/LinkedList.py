from node import Node

class LinkedList:
    def __init__(self, head):
        self.head = head    # type : Node

    def __str__(self):
        if self.head == None:
            return '[]'
        curr = self.head
        str_res= '['
        while curr != None:
            # print(str(curr.data))
            str_res +=   str(curr.data) +  ' -> ' 
            curr = curr.next
            
        return str_res[:-4] + ']'
    
    # inserts a the new data at the begining of the list
    def insertFirst(self, data = 'd' ):
        n1 = Node(data)
        n1.next = self.head
        self.head = n1
        
        
        
    def insertAtIndex(self, data, index):
        n1 = Node(data)
        if self.head == None:
            self.head = n1
        if index == 0 :
            self.insertFirst(data)
            
        curr = self.head
        i = 0
        while  curr != None and i < index:
            prev = curr 
            curr = curr.next
        # i have someone infront of me or None
        prev.next = n1
        n1.next = curr
        
        
        
        
    # ex 1 
    # insert an element 1 place after the head.
    # example-    lst: 1 -> 3 -> 9 
    #             lst.insertOneAfterHead(10)
    #             lst: 1 -> 10 -> 3 -> 9 
    def insertOneAfterHead(self, data): 
        n1 = Node(data)
        if self.head == None:
            self.head = n1
        n1.next = self.head.next 
        self.head.next = n1
        
            


    # ex 2: 
    # insert an at the end of the list
    # example-    lst: 1 -> 3 -> 9 
    #             lst.insertLast(10)
    #             lst: 1 -> 3 -> 9 -> 10
    def insertLast(self, data): 
        n1 = Node(data)
        if self.head == None:
            self.head = n1
            return
        curr = self.head
        while  curr.next != None:
            curr = curr.next
        curr.next = n1
        
    def remove_first_node(self):
        if self.head==None:
            return 
        self.head = self.head.next
    
    def remove_last_node(self):
        if self.head == None : 
            return
        if self.head.next == None : 
            self.head = None
            return
        
        curr = self.head
        while curr.next.next != None : 
            curr.next = None
    
    # ex3:
    # remove the element at the index given 
    #       lst: 1 -> 3 -> 9 
    #       lst.remove_at_index(1)
    #       lst: 1 -> 9
    def remove_at_index(self, index ) : # @TODO
        pass


if __name__ == '__main__':
    # n1 = Node(10)
    
    l1 = LinkedList(None)
    
    # n2 = Node(5)
    # n1.next = n2
    
    # n3 = Node(7)
    # n2.next = n3
    
    l1.insertLast( 4 )
    
    print (l1) 

    

    
    