# 프로그래머스 멀쩡한 사각형(210704)
# https://programmers.co.kr/learn/courses/30/lessons/62048
from math import gcd


def solution(w, h):
    answer = 1
    # w, h의 최대공약수 = 제거해야 할 모양이 반복되는 수
    gcd_val = gcd(w, h)

    if gcd_val == 1:
        answer = w + h - 1 # 최대 공약수가 1인 경우 사각형에서 나올 수 있는 멀쩡하지 않은 정사각형 면적
    else: # 최대공약수가 1이 아닌 경우
        # 반복되는 모양이 나올 수 있는 최소 사각형 구하기
        w_dash = w / gcd_val
        h_dash = h / gcd_val

        answer = gcd_val * (w_dash + h_dash - 1)

    answer = w * h - answer
    return answer

print(solution(8, 12))