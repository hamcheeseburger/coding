# 완주하지 못한 선수 level 1 정답
# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter

participant = ["mislav", "stanko", "mislav", "ana", "romi", "romi"]
completion = ["stanko", "ana", "mislav", "mislav", "romi"]

# 개선한 버전
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]

# # Sorting으로 풀기
# def solution(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[len(participant)-1]


print(solution(participant, completion))