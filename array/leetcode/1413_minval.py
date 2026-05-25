def min_val(nums):
    start_val = 1
    sum = start_val
    i = 0
    while i < len(nums):
        sum += nums[i]
        if sum == 0:
            start_val += 1
            i = 0
            sum = start_val
        elif sum < 0:
            start_val -= sum
            start_val += 1
            i = 0
            sum = start_val
        else:
            i = i + 1
    return start_val
            
nums = [-3,2,-3,4,2]
print(min_val(nums))