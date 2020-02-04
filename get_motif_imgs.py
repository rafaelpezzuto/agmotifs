import pygraphviz as pgv


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


ids_pga_e = [38, 74, 78, 92, 204, 206, 344, 392, 394, 408, 456, 472, 904, 906, 2186, 2190]
ids_pga = [38, 74, 76, 78, 92, 204, 206, 344, 394, 408, 456, 472, 904, 906, 2186, 2190, 2204, 2252, 2254]
ids_pa = [38, 74, 76, 78, 92, 204, 206, 344, 394, 408, 456, 472, 904, 906, 2186, 2190, 2204, 2252]

for c in set(ids_pga_e).union(set(ids_pga).union(ids_pa)):
    binvector = dec2bin(c)
    if c <= 38:
        size = 3
    elif c <= 31710:
        size = 4

    matrix = motif2adjmatrix(binvector, size)
    g = pgv.AGraph(directed=True)
    for i in range(size):
        g.add_node(i, shape='circle')
    for ind_i, i in enumerate(matrix):
        for ind_j, j in enumerate(i):
            if j == 1:
                g.add_edge(ind_i, ind_j)
    g.layout(prog='dot')
    g.draw('-'.join([str(size), str(c)]) + '.png')
