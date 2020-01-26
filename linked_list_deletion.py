#Deletion in the linked list

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Linked_list:
    def __init__(self):
        self.head = None
        
    def delete_from_end(self):
        current = self.head
        while(current.next):
            prev = current
            current = current.next
        prev.next = None
        current = None
        
        
    def delete_from_start(self):
        current = self.head
        self.head = current.next
        current None
        
    def at_any_point(self,pos):
        curr = self.head
        for i in range(0,pos):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr = None
        
        
        
        
            