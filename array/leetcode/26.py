def rem_dup(nums):
    n = len(nums)
    k = 0 
    i = 0
    for i in range(n):
        if i == n - 1:
            if nums[ i - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
            return k , nums
        if nums[i] != nums[i + 1]:
            nums[k] = nums[i]
            k += 1
            


nums = [1]
print(rem_dup(nums))