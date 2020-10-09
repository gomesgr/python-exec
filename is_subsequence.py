def is_subsequence(str1, str2):
    ptr1, ptr2 = 0, 0
    len1, len2 = len(str1), len(str2)

    while ptr1 < len1 and ptr2 < len2:
        if str1[ptr1] == str2[ptr2]:
            ptr1 += 1
            ptr2 += 1
        else:
            ptr1 += 1
    return ptr2 == len(str2)


print(is_subsequence('banana', 'nana'))
