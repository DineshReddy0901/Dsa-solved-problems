class MinStack(object):

    def __init__(self):
        self.s = []
        self.min_Stack = []

        

    def push(self, val):
        self.s.append(val)
        if not self.min_Stack:
            self.min_Stack.append(val)
        else:
            self.min_Stack.append(min(val,self.min_Stack[-1]))
        
        

    def pop(self):
        self.s.pop()
        self.min_Stack.pop()

        

    def top(self):
        return self.s[-1]
   
        

    def getMin(self):
        return self.min_Stack[-1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()