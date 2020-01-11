def add_matrices(a, b):
    # c = []
    # for i in range(len(a)):
    #     row = []
    #     for j in range(len(a[i])):
    #         row.append(a[i][j] + b[i][j])
    #     c.append(row)
    # return c

    c = []
    for row1, row2 in zip(a, b):
        c.append([x + y for x, y in zip(row1, row2)])
    return c

def sub_matrices(a, b):
    c = []
    for row1, row2 in zip(a, b):
        c.append([x - y for x, y in zip(row1, row2)])
    return c