class TwoSum(object):
      
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
            
    def find_keys(self, nums, target):
        self._bucket = len(nums)
        self._table = [[]for _ in range(self._bucket)]
        for items in nums:
            self.insert(items)
        
        for index in range(self._bucket):
            for i in range(len(self._table[index])):
                comp1 = self._table[index][i]
                comp2 = target - comp1
                hash  = self.hash_func(comp2)
                
                
                for a in range(len(self._table[hash])):
                    if hash == index:
                        if self._table[hash][a] == comp2 and a != i:
                            return comp1, comp2
                    else:
                        if self._table[hash][a] == comp2:
                            return comp1, comp2
        return False
    
    def twoSum(self, nums, target):
        if self.find_keys(nums, target) :
            key1, key2 = self.find_keys(nums, target)        
        else:
            print("No such keys found")
            return -1, -1 
        index1 = -1
        index2 = -1
        for i in range(len(nums)):
            if nums[i] == key1 and index1 == -1:
                index1 = i
                
            if nums[i] == key2 and i != index1:
                index2 = i              
        return index1, index2
    
    
nums = [2,7,11,15]
target = 9
bucket = len(nums)
two_sum = TwoSum()
print(two_sum.twoSum(nums, target))  