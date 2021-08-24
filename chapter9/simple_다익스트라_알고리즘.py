import sys

input = sys.stdin.readline
INF = int(1e9)

# n : 노드 개수, m : 간선 개수
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기 (a에서 b까지 가는 간선치가 c)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]: # 시작점과 연결된 노드들과의 간선치를 최단거리로 설정
        distance[j[0]] = j[1]

    for i in range(n - 1): # 시작 노드를 제외한 전체 노드에 대해 반복
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]: # j는 현재 노드와 연결된 노드들
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

print(distance)
