# 프로그래머스 소수찾기(210704)
# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


# 에라토스테네스의 체의 원리 사용
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
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