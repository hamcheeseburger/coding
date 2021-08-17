# chapter 5 실전문제 3

def travel(matrix, visited, row, col):
    visited[row][col] = True
    print(row , "," ,col)
    if col != 0:
        if matrix[row][col-1] == '0' and not visited[row][col-1]:
            travel(matrix, visited, row, col-1)

    if col != M-1:
        if matrix[row][col+1] == '0' and not visited[row][col+1]:
            travel(matrix, visited, row, col+1)

    if row != 0:
        if matrix[row-1][col] == '0' and not visited[row-1][col]:
            travel(matrix, visited, row-1, col)

    if row != N-1:
        if matrix[row+1][col] == '0' and not visited[row+1][col]:
            travel(matrix, visited, row+1, col)

    return


def findNotVisited(matrix, visited):
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and matrix[i][j] == '0':
                return i, j

    return -1, -1

first_line = input()
splited_first_line = first_line.split(" ")
N = int(splited_first_line[0])
M = int(splited_first_line[1])

matrix = []

for i in range(N):
    line = input()
    matrix.append(list(line))

print(matrix)

visited = [[False for col in range(M)] for row in range(N)]
print(visited)

count = 0
while True:
    i, j = findNotVisited(matrix, visited)
    if i == -1 and j == -1:
        break
    travel(matrix, visited, i, j)
    count += 1


print(visited)
print(count)
# 4 5
# 00110
# 00011
# 11111
# 00000