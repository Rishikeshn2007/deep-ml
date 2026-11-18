def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0])!=len(b):
        return -1
    row_a=len(a)
    cols_a=len(a[0])
    row_b=len(b)
    cols_b=len(b[0])
    c=[[0 for _ in range(cols_b)] for _ in range(row_a)]
    for i in range(row_a):
        for j in range(cols_b):
            for k in range(cols_a):
                c[i][j]+=a[i][k]*b[k][j]
    return c