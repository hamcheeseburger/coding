from collections import deque

n = int(input())

graph = [[] for i in range(n + 1)] # 선수과목 관계
cost = [0] * (n+1) # 해당 과목 수강 시간
income_cost = [0] * (n+1) # 진입차수
for i in range(1, n + 1):
    input_list = list(map(int, input().split()))
    cost[i] = input_list[0]
    for j in range(1, len(input_list)):
        if input_list[j] != -1:
            graph[input_list[j]].append(i)
            income_cost[i] += 1

deq = deque()

for i in range(1, n + 1):
    if income_cost[i] == 0:
        deq.append(i)

result = [0] * (n + 1)

for ele in deq: # 처음 deq에 들어가는 과목들에 해당하는 총 수강 시간을 초기화함
    result[ele] = cost[ele]

while deq:
    ele = deq.popleft()
    for connected in graph[ele]:
        income_cost[connected] -= 1
        result[connected] = result[ele] + cost[connected]

        if income_cost[connected] == 0:
            deq.append(connected)

print(result)