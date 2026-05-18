def prefix_sum(array):
    n = len(array)
    prefix_sum = [0]*n
    prefix_sum[0] = array[0]
    for i in range(1, n):
        prefix_sum[i] = array[i] + prefix_sum[i - 1]
    return prefix_sum


arr = [10,25,30,14,68]
print(prefix_sum(arr))