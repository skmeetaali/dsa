class Queue():
    def __init__(self,size):
        self.front = 0
        self.rear = -1
        self.size = size
        self.arr = [0] * self.size
        
    def push(self, d):
        if self.rear == self.size  and self.front == 0:
            print("queue is full")
            return
        
        if self.rear == self.front :
            print("queue is full here")
            return
        
        if self.rear == self.size and self.front != 0:
            self.rear = 0
        
        if self.rear == -1:
            self.rear = 0
        
        self.arr[self.rear] = d
        print(self.rear, f"inserted {self.arr[self.rear]} rear : {self.rear} front : {self.front}")
        self.rear += 1

        
    def pop(self):
        
        if self.rear == -1:
            print("cantpop queue is empty")
        
        if self.front == self.size - 1:
            val = self.arr[self.front]
            if self.rear == 0:
                self.rear = -1
            self.front = 0
            return val
            
        
        val = self.arr[self.front]
        if self.front == self.rear - 1:
            self.rear = -1
            self.front = 0
            return val
        self.front += 1
        return val

    def getfront(self):
        if self.rear == -1:
            print("queue empty")
            
        return self.arr[self.front]
    
    
    def getrear(self):
        if self.rear == -1:
            print("queue empty")
            
        return self.arr[self.rear - 1]

if __name__ == '__main__':
    q = Queue(5)
    q.push(12)    
    q.push(3)
    q.push(17)
    q.push(12)    
    q.push(9)
    q.pop()
    q.push(17)
    q.push(24)
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.pop()


    print(q.getfront(),q.front, q.getrear(), q.rear)