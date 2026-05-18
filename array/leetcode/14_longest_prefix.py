def longest_prefix(array):
    longest_prefix = ""
    j_range = len(array[0])
    n = len(array)
    try:
        for j in range(j_range):
            for i in range(n - 1):
                if array[i][j] == array[i + 1][j]:
                    pass
                else:
                    return longest_prefix
            longest_prefix += array[0][j]
        return longest_prefix
    except Exception as e:
        return longest_prefix
    
strs = ["dog","racecar","car"]
print(longest_prefix(strs))