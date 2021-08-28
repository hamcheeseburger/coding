import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# n : 노드 개수, m : 간선 개수
n, m = map(int, input().split())

distance = [INF] * (n + 1)

node_edge_mapping = []
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

# 모든 간선 정보 입력 받기 (a에서 b까지 가는 간선치가 c)
for _ in range(m):
    a, b, c = map(int, input().split())
    node_edge_mapping.append((c, a, b))
node_edge_mapping.sort()


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def isCycle(parent, a, b):
    if find_parent(parent, a) == find_parent(parent, b):
        return True

    return False

result = 0
for element in node_edge_mapping:
    cost = element[0]
    a = element[1]
    b = element[2]

    if isCycle(parent, a, b):
        continue

    union_parent(parent, a, b)
    result += cost

print(parent)
print(result)