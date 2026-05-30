class Solution(object):
    map = {
        '2': ['a', 'b','c'],
        '3': ['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o',],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }
    result = []
    i = 0
    j = 0
    def letterCombinations(self, digits):
        return self.results(self, digits , 0, 0)
        
    def results(self, digits,i, j):
        n = len(digits)
        if self.i == len(digits):
            return self.result
        if self.j == len(map.get(digits[i])):
            return self.results(self, digits, i + 1, 0)

                

