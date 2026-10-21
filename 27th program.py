i = 4
rows = i
cols = i

matrix =  []
for r in range(rows):
    row =[]
    for c in range(cols):
        row.append(0)
    matrix.append(row)
for row in matrix:
    print(''.join(map(str, row)))