bucket = 6
class HASH(object):
    def __init__(self, bucket):
        self._bucket = bucket
        self._table = [[]for _ in range(self._bucket)]
        
        
    def hash_func(self, key):
        return key % self._bucket
    
    def insert(self, key):
        index = self.hash_func(key)
        self._table[index].append(key)
        
    def delete(self, key):
        index = self.hash_func(key)
        if key not in self._table[index]:
            return
        
        self._table[index].remove(key)
        
    def display(self):
        for index in range(self._bucket):
            print(index, end=" ")
            for item in self._table[index]:
                print("-->", item, end=" ")
            print()
                
a = [12,4,16,7,0,6]
hash_table = HASH(len(a))

for x in a :
    hash_table.insert(x)
    
hash_table.display()