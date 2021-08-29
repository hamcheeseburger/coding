import sys

input = sys.stdin.readline

# n : 노드 개수, m : 간선 개수
n, m = map(int, input().split())

node_edge_mapping = []
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

# 모든 간선 정보 입력 받기 (a에서 b까지 가는 간선치가 c)
for _ in range(m):
    a, b, c = map(int, input().split())
    node_edge_mapping.append((c, a, b))
node_edge_mapping.sort()


def find_root_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_root_parent(parent, parent[a])

    return parent[a]


def union_parent(parent, a, b):
    a = find_root_parent(parent, a)
    b = find_root_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def isCycle(parent, a, b):
    if find_root_parent(parent, a) == find_root_parent(parent, b):
        return True

    return False

result = 0
selected = []
for node_edge in node_edge_mapping:
    cost = node_edge[0]
    a = node_edge[1]
    b = node_edge[2]

    if isCycle(parent, a, b):
        continue

    union_parent(parent, a, b)
    result += cost
    selected.append(cost)

print(selected)
print(result - max(selected)) # 두 마을을 분리하는 방법 = 일단 최소신장트리를 만들고 간선 중 제일 큰 값을 갖는 간선 하나을 제거하면 마을이 2개로 분리된다

