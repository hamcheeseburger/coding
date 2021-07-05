from itertools import permutations


def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2)) # 집합에서 0,1 제외
    # 소수 아닌 것 제외 (에라토스테네스의 체 공부할 것)
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i)) # i의 배수 제외
    return len(a)


print(solution('33'))