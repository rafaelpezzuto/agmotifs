def dec2bin(num: int):
    chrs = []
    while num > 0:
        chrs.append(int(num % 2))
        num = int(num / 2)
    return chrs


def motif2adjmatrix(vector: list, size: int):
    matrix = [[0] * size for i in range(size)]
    line_counter = 0
    column_counter = 0
    for index, i in enumerate(vector):
        if (index) % size == 0 and index != 0 and index != size - 1:
            line_counter += 1
            column_counter = 0
        matrix[line_counter][column_counter] = i
        column_counter += 1
    return matrix


def print_matrix(matrix):
    for i in matrix:
        for ii in i:
            print(ii, '\t', end='')
        print()


c3 = [38]

c4_1 = set([74, 78, 92, 204, 206, 344, 394, 408, 904, 2186])
c4_2 = set([74, 78, 92, 204, 206, 344, 394, 408, 456, 904, 2186])
c4_3 = set([74, 78, 92, 204, 206, 344, 394, 408, 456, 904, 2186])
c4_4 = set([74, 78, 92, 204, 206, 344, 392, 394, 408, 904])
c4 = sorted(c4_1.union(c4_2).union(c4_3).union(c4_4))

c5_1 = set([154, 158, 188, 406, 412, 414, 444, 924, 926, 1298, 1306, 1802, 1816, 1818, 1832, 3344, 3352, 8470, 8474, 8504, 8594, 8624, 8730, 8734, 8756, 8760, 8852, 8856, 8984, 41490, 49670, 49682])
c5_2 = set([154, 156, 158, 184, 188, 406, 412, 414, 444, 924, 926, 1208, 1298, 1304, 1306, 1328, 1424, 1456, 1802, 1816, 1832, 3344, 3346, 3352, 8466, 8470, 8496, 8594, 8596, 8624, 8728, 8730, 8756, 8760, 8852, 35344])
c5_3 = set([154, 158, 184, 188, 406, 412, 414, 444, 924, 926, 1208, 1306, 1328, 1336, 1456, 1802, 1816, 1818, 1832, 1848, 3344, 3346, 3352, 3864, 8466, 8470, 8474, 8496, 8504, 8594, 8596, 8600, 8624, 8728, 8730, 8734, 8756, 8760, 8852, 8854, 8856, 8860, 8888, 34192, 35120, 35346, 41490, 41520, 42512, 43536, 49670, 49808])
c5 = sorted(c5_1.union(c5_2).union(c5_3))

for c in c3:
    print(c)
    binvector = dec2bin(c)
    matrix = motif2adjmatrix(binvector, 3)
    print_matrix(matrix)
