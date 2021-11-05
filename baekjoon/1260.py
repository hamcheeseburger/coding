from collections import deque


def dfs(graph, v):
    stack = [v]
    result = []
    while stack:
        ele = stack.pop()
        if ele not in result:
            result.append(ele)
        for vertex in graph[ele]:
            if vertex not in result:
                stack.append(vertex)

    for i in result:
        print(i, end=' ')
    print()


def bfs(graph, v):
    deq = deque([v])
    result = []
    while deq:
        ele = deq.popleft()
        if ele not in result:
            result.append(ele)
        for vertex in graph[ele]:
            if vertex not in result:
                result.append(vertex)
                deq.append(vertex)
    for i in result:
        print(i, end=' ')


N, M, V = map(int, input().split())
matrix = [[] for _ in range(N+1)]

for i in range(M):
    V1, V2 = map(int, input().split())
    matrix[V1].append(V2)
    matrix[V2].append(V1)

for i in range(N+1):
    matrix[i].sort(reverse=True)
dfs(matrix, V)

for i in range(N+1):
    matrix[i].sort()
bfs(matrix, V)
