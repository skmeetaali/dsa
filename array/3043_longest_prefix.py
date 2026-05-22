def longest_prefix(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    max_prefix_len = 0
    for i in range(n):
        print(arr1[i])
        pref_len = 0
        num1 = str(arr1[i])
        n1 = len(num1)
        for j in range(m):
            num2 = str(arr2[j])
            for k in range(n1):
                if k >= len(num2):
                    break
                if num1[k] == num2[k]:
                    pref_len += 1
                    if max_prefix_len < pref_len:
                        max_prefix_len = pref_len
                else:
                    pref_len = 0
                    break
            pref_len = 0

                    
    return max_prefix_len

arr1 = [1,10,100]
arr2 = [1000]
print(longest_prefix(arr1, arr2))