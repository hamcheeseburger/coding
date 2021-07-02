# 프로그래머스 타겟넘버(210702)
# https://programmers.co.kr/learn/courses/30/lessons/43165

def check(numbers, sum_num, start, end, target):
    if start == end:
        if sum_num == target:
            return 1
        else:
            return 0

    rslt1 = check(numbers, sum_num + numbers[start], start + 1, end, target)
    rslt2 = check(numbers, sum_num - numbers[start], start + 1, end, target)

    return rslt1 + rslt2


def solution(numbers, target):
    return check(numbers, 0, 0, len(numbers), target)

# 다른 풀이
# target에서 원소들을 빼고 더하는 경우의 수로..
# def check(numbers, start, end, target):
#     if start == end:
#         if target == 0:
#             return 1
#         else:
#             return 0
#
#     rslt1 = check(numbers, start + 1, end, target - numbers[start])
#     rslt2 = check(numbers, start + 1, end, target + numbers[start])
#
#     return rslt1 + rslt2
#
#
# def solution(numbers, target):
#     return check(numbers, 0, len(numbers), target)

