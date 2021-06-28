# 프로그래머스 124 나라의 숫자 (210628)
# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    match_list = [4, 1, 2]
    size = 1
    num = 0

    while n > ((3**size) + num):
        num = 3**size
        size += 1

    # print(size)
    s = ""
    n_copy = n
    for i in range(size):
        portion = (n_copy-1) // 3
        rest = n_copy % 3
        # print("rest : " , rest)
        s += str(match_list[rest])
        n_copy = portion

    answer = s[::-1]
    return answer

print(solution(12))