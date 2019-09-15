input = [[0,1, 0],[0,0, 0],[0,0,0]]
row = [0] * 3
col = [0] * 3
print (row)
for i in range(3):
    row[i] = 0
for  j in range(3):
    col[j]  = 0
print (col)       
for i in range(3):
    for j in range(3):
        if input[i][j] == 1:
            row[i] =1
            col[j] =1
print (row, col)            

for i in range(3):
    for j in range(3):
        if row[i] == 1 or  col[j] == 1:
            input[i][j] = 1

print (input)            