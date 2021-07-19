# 프로그래머스 튜플(210719)
# https://programmers.co.kr/learn/courses/30/lessons/64065

import re


def solution(s):
    size = len(s)
    s = s[1:size - 1]
    s = re.split('},', s) # '},'로 구분하기!! (붙어있는 문자로 구분하고 싶을 떄 사용)
    s.sort(key=len) # 길이로 정렬하기

    answer_list = []

    for ele in s:
        num_list = re.findall("\d+", ele) # 숫자만 뽑아내기
        for num in num_list:
            if int(num) not in answer_list: # 정답 리스트에 원소가 이미 존재한다면 append하지 않기
                answer_list.append(int(num))

    return answer_list

