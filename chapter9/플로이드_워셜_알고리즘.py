# 출발 노드에서 전체 노드까지 갈 수 있는 최단 경로를 찾되, 출발 노드가 전체 노드가 되는 것.
import sys
input = sys.stdin.readline
INF = int(1e9)

# n : 노드 개수, m : 간선 개수
n = int(input())
m = int(input())

matrix = []
for i in range(n + 1):
    matrix.append([INF] * (n + 1))

# 모든 간선 정보 입력 받기 (a에서 b까지 가는 간선치가 c)
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a][b] = c
    matrix[a][a] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

print(matrix)
