src = (2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11)
result = []
for num in src:
    temporary_val = 0
    for i in range(len(src)):
        if num == src[i]:
            temporary_val += 1

    if temporary_val == 1:
        result.append(num)

print(result)
