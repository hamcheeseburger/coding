# getSmallestNode()와 visited 배열이 사라짐
# getSmallestNode() => heapq(우선순위큐)로 대체


import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# n : 노드 개수, m : 간선 개수
n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기 (a에서 b까지 가는 간선치가 c)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    pqueue = []
    heapq.heappush(pqueue, (0, start))

    distance[start] = 0
    while pqueue: # 시작 노드를 제외한 전체 노드에 대해 반복
        dist, now = heapq.heappop(pqueue)

        if distance[now] < dist: # 현재 노드까지의 최단 거리를 찾는 것이기 때문에.. 최소값이 갱신이 되지 않으면 더 볼 필요가 없음
            continue

        for j in graph[now]: # j는 현재 노드와 연결된 노드들
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(pqueue, (cost, j[0])) # (비용, 노드) => 노드까지 도달하는 비용

dijkstra(start)

print(distance)