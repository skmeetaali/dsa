class Solution(object):
    
    def hash_func(self, key, n):
        return key % n
    
    def insert(self, key, n):
        index = self.hash_func(key, n)
        self._table[index].append(key)
        
    def missingNumber(self, nums):      
        n = len(nums)
        self._table = [[] for _ in range(n)]
        
        for i in range(n):
            self.insert(nums[i], n)
            
        if n not in self._table[0]:
            return n
        
        for i in range(n):
            if i not in self._table[i]:
                return i
        
        
nums = [8,6,4,2,3,5,7,0,1]
sol = Solution()
print(sol.missingNumber(nums))