from collections import deque
# 인접 행렬 방식
info = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
q = deque()


def bfs(node):
    if visited[node] is False:
        visited[node] = True
        print(node, end=' ')
    else:
        q.popleft()

    for n in info[node]: # 자식 노드 방문
        if visited[n] is False:
            visited[n] = True
            q.append(n)
            print(n, end=' ')

    if len(q) != 0: # 제일 왼쪽에 있던 자식 부터 다시 bfs 시작
        bfs(q[0])


bfs(1)
