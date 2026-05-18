def smi(array):
    n = len(array)
    max_pref_len = 1
    max_pref_sum = array[0]
    pref_len = array[0]
    pref_sum = array[0]
    for i in range(1, n):
        print(pref_sum)
        if array[i] == array[i - 1] + 1:
            pref_len += 1
            pref_sum += array[i]
            print(pref_sum, "whyyy")
            if pref_len > max_pref_len:
                max_pref_len = pref_len
                max_pref_sum = pref_sum
        else:
            break
            
    if max_pref_sum not in array:
        print("hey")
        print(max_pref_sum)
        return max_pref_sum
    else:
        while True:
            max_pref_sum += 1
            if max_pref_sum not in array:
                print("hi")
                print(max_pref_sum)
                return max_pref_sum
            else:
                continue
    
nums =[37,1,2,9,5,8,5,2,9,4]
print(smi(nums))