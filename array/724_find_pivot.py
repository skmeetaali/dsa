def pivot_index(nums):
    right_sum = 0
    left_sum = 0
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0
    #calculate right_sum
    for i in range(len(nums)):
        right_sum += nums[i]
        
    right_sum -= nums[0]
    if left_sum == right_sum:
        return 0
    
    for i in range(1,len(nums)):
        right_sum -= nums[i]
        left_sum += nums[i-1]
        print(left_sum, right_sum)
        if left_sum == right_sum:
            return i
    return -1
nums = [1,7,3,6,5,6]
print(pivot_index(nums))