# Insertion and Deletion in a stack




class stack:
    def __init__(self):
        self.list=[]
    
    def push(self,a):
        self.list.append(a)
    def pop(self):
        self.list.pop()
    def isEmpty(self):
        return self.list==[]
    def top(self):
        if not self.isEmpty():
            return self.list[-1]
    def getStack(self):
        return self.list
            
            
s= stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
print(s.getStack())
s.pop()
s.pop()
s.pop()
print(s.getStack())
print(s.top())
print(s.isEmpty())