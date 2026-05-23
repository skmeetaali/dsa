def rem_dup(nums):
    n  = len(nums)
    if n < 2:
        return n, nums
    ptr1 = 0
    ptr2 = 1
    new = []
    for _ in range(len(nums)):
        print("hey")
        if ptr2 >= n:
            new.append(nums[ptr1])
            break
        if nums[ptr1] != nums[ptr2]:
            new.append(nums[ptr1])
            new.append(nums[ptr2])
            ptr1 += 1
            ptr2 += 1
        else:
            new.append(nums[ptr2])
            ptr1 += 1
            ptr2 += 1
            while True:
                if ptr2 >= n:
                    break
                if nums[ptr1] == nums[ptr2]:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    break
            ptr1 += 1
            ptr2 += 1
    m = len(new) 
    return new

nums =[1,1,2]
print(rem_dup(nums))