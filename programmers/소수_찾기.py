# 프로그래머스 소수찾기(210704)
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def prime_number(number):
    if number <= 1:
        return False

    for f in range(2, number):
        if number % f == 0:
            return False

    return True


def solution(numbers):
    answer = 0
    numbers = list(numbers)

    set_list = []
    for n in range(1, len(numbers) + 1):
        permutation_list = list((map(''.join, permutations(numbers, n))))

        permutation_list = list(map(int, permutation_list))

        set_list += permutation_list

    set_list = set(set_list)
    for ele in set_list:
        if prime_number(ele):
            answer += 1

    return answer