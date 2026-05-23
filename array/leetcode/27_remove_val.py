def remove_val(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    k += 1
    return k, nums

nums = [0,1,2,2,3,4,3]
val = 3
print(remove_val(nums, val))