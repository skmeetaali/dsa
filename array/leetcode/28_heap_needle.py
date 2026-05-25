def first_index(haystack, needle):
    if len(needle) == 0 or len(haystack) == 0:
        return -1
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            j = i
            for k in range(len(needle)):
                if k == len(needle)-1:
                    return i
                if haystack[j] == needle[k]:
                    j += 1
                else:
                    break
    print("here at last")
    return -1


haystack = "sadbutsad"
needle = "sad"
print(first_index(haystack, needle))