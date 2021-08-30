# p.298
def find_root_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_root_parent(parent, parent[a])

    return parent[a]


def union(parent, a, b):
    a = find_root_parent(parent, a)
    b = find_root_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


node, inputCount = map(int, input().split())

parent = [0] * (node + 1)

for i in range(1, node + 1):
    parent[i] = i

for _ in range(inputCount):
    cmd, a, b = map(int, input().split())

    if cmd == 0:
        union(parent, a, b)
    else:
        if find_root_parent(parent, a) == find_root_parent(parent, b):
            print("YES")
        else:
            print("NO")
