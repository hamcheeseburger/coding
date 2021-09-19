def dfs(start, info, binary, lamb, wolf):
    if info[start] == 0:
        lamb += 1
    else:
        wolf += 1

    print(start, lamb, wolf)

    if lamb - wolf <= 0:
        return lamb, wolf

    for child in binary[start]:
        if info[child] == 1:
            if lamb - (wolf + 1) <= 0:
                continue

        lambVal, wolfVal = dfs(child, info, binary, lamb, wolf)
        if lamb < lambVal:
            lamb = lambVal

    return lamb, wolf


def solution(info, edges):
    binary = [[] for i in range(len(info))]
    visited = [0] * len(info)
    for edge in edges:
        binary[edge[0]].append(edge[1])

    print(binary)
    print(info)

    lamb, wolf = dfs(0, info, binary, 0, 0)
    print(lamb, wolf)

    return 0


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
print(solution(info, edges))
