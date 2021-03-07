src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(len(src)):
    next_indx = i + 1
    if src[i] != src[-1]:
        if src[i] < src[next_indx]:
            result.append(src[next_indx])

print(result)

