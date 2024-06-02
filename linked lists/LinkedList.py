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
    def remove_at_index(self, index ) : # אינקסים קטנים\גדולים מאורך המערך לא תופסים
        if self.head == None : 
            return None
        x = self.head
        i = 0
        while i < index - 1:
            x = x.next
            i+=1
        x.next = x.next.next
        
    # This method returns the index of the first occurrence
    # of the specified element in this list,
    # or -1 if this list does not contain the element.
    # example
    #       lst: 1 -> 3 -> 9 
    #       lst.index_of(1)
    #       lst: 1 -> 9
    
    def index_of(self, element):
        i = 0 
        pos = self.head
        while pos != None:
            if pos.data == element:
                return i 
            i += 1 
            pos = pos.next
        
        return -1
    
    # This method returns the index of the last occurrence of
    # the specified element in this list, or -1
    # if this list does not contain the element.
    # example
    #       lst: 1 -> 3 -> 9 -> 1
    #       lst.last_index_of(1)
    #       3
    
    def last_index_of(self, element):
        i = 0
        pos = self.head
        last = -1
        while pos != None:
            if pos.data == element:
                last = i 
            i += 1
            pos = pos.next
        return last

    #This method returns a deep copy of this LinkedList.
    # example
    #       lst: 1 -> 3 -> 9 -> 1
    #       x = lst.deep_copy()
    #       'x' is actually identical to 'lst' but is a different LinkedList.
    def deep_clone(self): # @TODO
       pass
    def element_count_in_list(self,element):
        pos = self.head
        count = 0
        while pos != None:
            if pos.data == element:
                count += 1
            pos = pos.next
        return count
        

       


if __name__ == '__main__':
    
    
    n1 = Node(1)
    n2 = Node(3)
    n1.next = n2

    y = n1 # shallow copy
    
    x = Node(1) # deep copy
    x.next = n2
    
    
    
    
    
    n2 = Node(3)
    n3 = Node(9)
    n4 = Node(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    l1 = LinkedList(n1)
    # [1 -> 3 -> 9]
    
    
    
    
    
    print (l1.element_count_in_list(9))
    print (l1) 

    

    
    