class Node:
    def __init__(self, data):
        self.d = data
        self.next = None
        
class Stack():
    def __init__(self):
        self.top = None
        self.count = 0
    
    def push(self, d):
        node = Node(d)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.top == Node:
            print("stack underflow")
            return
        last = self.top
        self.top = last.next
        self.count -= 1
        val = last.d
        del last
        return val
    
    def peek(self):
        if self.top == None:
            print("stack empty")
            return
        return self.top.d
    
    def isEmpty(self):
        return self.top == None
    
    def size(self):
        return self.count
    
    
if __name__ == "__main__":
    s = Stack()
    print("stack is empty? ", s.isEmpty())

    s.push(8)
    s.push(7)    
    s.push(11)
    s.push(4)
    s.push(9)
    s.pop()
    s.push(0)
    s.push(8)
    s.push(7)    
    s.push(11)
    s.push(4)
    s.push(9)
    print("stack size: ", s.size())