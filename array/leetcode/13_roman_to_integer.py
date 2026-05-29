class Solution(object):
    def romanToInt(self, s):
        number = 0
        dict = {
            'I': 1,
            'V': 5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        for i in range(len(s)):
            if i == len(s) - 1:
                return number + dict.get(s[i])
            current = dict.get(s[i])
            next = dict.get(s[i+1]) 
            
            if current < next:
                number -= current
            else:
                number += current    
    
    
s = "MCMXCIV"
sol = Solution()
print(sol.romanToInt(s))
                    
