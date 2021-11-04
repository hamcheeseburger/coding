from collections import deque


def bfs(list_map, col, row, M, N):
    if not list_map[row][col]:
        return False

    visit_list = deque([(row, col)])
    while visit_list:
        tup = visit_list.popleft()

        row = tup[0]
        col = tup[1]
        list_map[row][col] = 0
        if row < N - 1 and list_map[row+1][col] and (row + 1, col) not in visit_list:
            visit_list.append((row + 1, col))
        if row > 0 and list_map[row-1][col] and (row - 1, col) not in visit_list:
            visit_list.append((row - 1, col))
        if col < M - 1 and list_map[row][col+1] and (row, col+1) not in visit_list:
            visit_list.append((row, col+1))
        if col > 0 and list_map[row][col-1] and (row, col-1) not in visit_list:
            visit_list.append((row, col-1))

    return True


testcase = int(input())

result_list = []
for i in range(testcase):
    M, N, K = map(int, input().split())
    list_map = [[0]*M for _ in range(N)]
    for j in range(K):
        col, row = map(int, input().split())
        list_map[row][col] = 1

    result = 0
    for row in range(N):
        for col in range(M):
            if bfs(list_map, col, row, M, N):
                result += 1
    result_list.append(result)

for result in result_list:
    print(result)


