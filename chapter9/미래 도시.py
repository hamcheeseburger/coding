# 문제 조건에서 n <= 100 이라고 했으므로 플로이드 워셜 문제로도 충족시킬 수 있음
# 간단하게 풀수있는 건 플로이드 워셜로 풀자

import sys
input = sys.stdin.readline
INF = int(1e9)

# n : 노드 개수, m : 간선 개수
n, m = map(int, input().split())

matrix = []
for i in range(n + 1):
    matrix.append([INF] * (n + 1))

# 모든 간선 정보 입력 받기 (a에서 b까지 가는 간선치가 c)
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

x, k = map(int, input().split()) # 거쳐갈 곳 (k), 목적지(x)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

val = matrix[1][k] + matrix[k][x]

if val >= INF:
    print(-1)
else:
    print(val)