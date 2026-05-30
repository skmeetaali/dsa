class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ptr1 = 0
        ptr2 = 0
        if m == 0:
            for i in range(n):
                nums1[ptr1] = nums2[ptr2]
                ptr1 += 1
                ptr2 += 1
            return
                
        if n == 0:
            return    

        for i in range(len(nums1)):
            if  nums1[ptr1] == 0:
                nums1[ptr1] = nums2[ptr2]
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1] != 0 and nums1[ptr1] <= nums2[ptr2]:
                ptr1 += 1
            else:
                temp_ptr2 = ptr2
                while temp_ptr2 < n  and nums2[temp_ptr2] < nums1[ptr1] :
                    temp_ptr2 += 1
                for ptr2 in range(temp_ptr2):
                    temp = nums1[ptr1]
                    nums1[ptr1] = nums2[ptr2]
                    nums2[ptr2] = temp
                    ptr1 += 1
                    ptr2 += 1
                

                
nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
sol = Solution()
sol.merge(nums1,m, nums2, n)
print(nums1)