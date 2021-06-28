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

def dfs(node):
    if visited[node]:
        return

    # 방문표시
    visited[node] = True
    print(node, end=" ")

    for n in info[node]:
        dfs(n)


dfs(1)