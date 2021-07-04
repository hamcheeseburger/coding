# 프로그래머스 더 맵게(210629)
# https://programmers.co.kr/learn/courses/30/lessons/42626#

import heapq

# def check(scoville, K, count):

#     if scoville[0] >= K:
#         return count

#     if len(scoville) == 1:
#         return -1

#     first = heapq.heappop(scoville)
#     second = heapq.heappop(scoville)
#     new_ele = first + (second * 2)

#     heapq.heappush(scoville, new_ele)
#     count += 1

#     return check(scoville, K, count)

def solution(scoville, K):
    heapq.heapify(scoville)

    # return check(scoville, K, 0)

    count = 0
    while True:
        if scoville[0] >= K:
            return count
        if len(scoville) == 1:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_ele = first + (second * 2)

        heapq.heappush(scoville, new_ele)
        count += 1
