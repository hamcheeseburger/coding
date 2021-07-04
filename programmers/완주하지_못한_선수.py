# 완주하지 못한 선수 level 1
# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

participant = ["mislav", "stanko", "mislav", "ana", "romi", "romi"]
completion = ["stanko", "ana", "mislav", "mislav", "romi"]


def solution(participant, completion):
    parCounter = dict(Counter(participant))
    comCounter = dict(Counter(completion))
    for com in comCounter:
        parCounter[com] -= comCounter[com]
        if parCounter[com] == 0:
            del parCounter[com]

    parCounter = list(parCounter.keys())
    return parCounter[0]


print(solution(participant, completion))
