def next_greater(num):
    digits = list(str(num))
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
        if i == -1:
            return num
    j = len(digits) - 1

    while digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits[i+1:] = digits[:i:-1]
    return int(''.join(digits))

v = 213

print(next_greater(v))