import sys
from collections import deque

deq = deque()
input = sys.stdin.readline

# n : 노드 개수, m : 간선 개수
n, m = map(int, input().split())

income_count = [0] * (n + 1) # 진입 차수
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    income_count[b] += 1


print(income_count)
print(graph)

result = []


def topology():
    for i in range(1, n + 1):
        if income_count[i] == 0:
            deq.append(i)

    while len(deq) != 0:
        print(deq)
        ele = deq.popleft()
        result.append(ele)
        for connected in graph[ele]:
            income_count[connected] -= 1 # 어차피 연결된 노드의 진입 차수를 변경하므로
            if income_count[connected] == 0: # 진입차수가 0이 되는 것도 연결된 노드들 중 나올 것
                deq.append(connected)


topology()

print(result)





