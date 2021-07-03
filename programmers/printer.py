# 프로그래머스 프린터(210703)
# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    queue = []

    # tuple화 (location을 쉽게 찾기 위함)
    for i in range(len(priorities)):
        queue.append((i, priorities[i]))

    # popleft()를 하기 위해 덱화
    # queue(list)의 pop(0)의 시간 복잡도는 N,
    # deque의 popleft()의 시간복잡도는 1이다.
    queue = deque(queue)

    stack = []
    while True:
        ele = queue.popleft()
        origin_len = len(queue)

        # 작업큐에 남아있는 것 중 더 우선순위가 높은 작업이 있는지 확인
        i = 0
        while i < origin_len:
            if queue[i][1] > ele[1]:
                break
            i += 1

        # 더 높은 우선순위가 있는 경우
        if i != origin_len:
            queue.append(ele)
        # 더 높은 우선순위가 없는 경우
        else:
            stack.append(ele)
            if ele[0] == location: # 현재 프린트된 유인물이 내가 찾는 것이라면 break
                break
    # print(queue)
    # print(queue)
    # print(stack)

    return len(stack)