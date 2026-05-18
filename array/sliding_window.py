def sliding_wnd(array, k):
    curr_wdn = 0
    for i in range(k):
        curr_wdn +=  array[i]
    n = len(array)
    max_wdn = curr_wdn
    for i in range(k, n):
        curr_wdn = curr_wdn - array[i - k] + array[i]
        if max_wdn < curr_wdn:
            max_wdn = curr_wdn
    return max_wdn


array = [10,4,15,0,23,6]
print(sliding_wnd(array, 3))