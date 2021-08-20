# bfs로 풀어야 하는 문제

# 공백구분으로 입력 받기
from collections import deque

N, M = map(int, input().split())

matrix = []
for i in range(N):
    matrix.append(list(map(int, input()))) # 입력받은 문자열의 문자들 각각 int 변환, 리스트화

print(matrix)

x_direction = [-1, 1, 0, 0]
y_direction = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 모든 경우를 따져야 하기 때문에

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + x_direction[i]
            ny = y + y_direction[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if matrix[nx][ny] == 0:
                continue

            if matrix[nx][ny] == 1: # 해당 위치에 첫 방문
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

    return matrix[N-1][M-1]


print(bfs(0, 0))

