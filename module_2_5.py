def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        l = []
        matrix.append(l)
        for j in range(m):
            l.append(value)
    return matrix


result1 = get_matrix(2, 2, 43)
result2 = get_matrix(2, 8, 14)
result3 = get_matrix(4, 5, 9)
print(result1)
print(result2)
print(result3)






