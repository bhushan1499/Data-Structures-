Insertion in linked list
  
  
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = node(data)
        
        if self.head is None:
            self.head = new_node
            return 
        
            last_node = self.head
            while(last_node.next):
                last_node = last_node.next
                last_node.next = new_node
    def prepend(self,data):
        new_node = node(data)
        
        new_node.next = self.head
        self.head = new_node
    
    def insertafter(self,data,pos):
        new_node = node(data)
        curr = self.head
       
        for i in range(pos-1):
            curr = curr.next
            nxt = curr.next
        curr.next = new_node
        newnode.next = nxt    
    
    
    
    
                
    def printlist(self):
        current = self.head
        while(current):
            print(current.data)
            current=current.next
            
            
            
            
lis = Linked_list()
lis.append(10)
lis.append(20)
lis.append(30)
lis.append(40)
lis.append(50)
lis.append(60)
lis.printlist()

                