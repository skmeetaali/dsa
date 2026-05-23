def con_dup(arr, win):
    if len(arr) <= win:
        for j in range(len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if arr[j] == arr[k]:
                    return True
    else:
        for i in range(len(arr) - win):
            print(i)
            for j in range(i, i + win ):
                print(j)
                for k in range(j + 1, i + win + 1):
                    print(k, "k")
                    if arr[j] == arr[k]:
                        return True
            print("brk")
            
    return False

nums = [99,99]
k = 2
print(con_dup(nums, k))