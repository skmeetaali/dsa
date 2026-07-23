class Stack:
    def __init__(self, cap):
        self.cap = cap
        self.arr = [0] * self.cap
        self.top = -1
        
    def push(self, elem):
        if self.top == self.cap - 1:
            print("stack full")
            return
        
        self.top += 1
        self.arr[self.top] = elem
        print(f"pushed {self.arr[self.top]}")
        
    def pop(self):
        if self.top == -1:
            print("stack underflow")
            return
        val = self.arr[self.top]
        self.top -= 1
        return val
    
    def peek(self):
        if self.top == -1:
            print("stack empty")
            return
        
        return self.arr[self.top]
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.cap -1
    
if __name__ == "__main__":
    s = Stack(5)
    print("stack is full ? ",s.isFull(),"\nstack is empty? ", s.isEmpty())

    s.push(8)
    s.push(7)    
    s.push(11)
    s.push(4)
    s.push(9)
    s.pop()
    s.push(0)
    print("stack is full ? ",s.isFull(),"\n stack is empty? ", s.isEmpty())
    