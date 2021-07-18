# 프로그래머스 [1차] 뉴스클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

import math


def makeSplit(string): # 문자열을 순차적으로 2개씩 나누는 과정
    string = string.lower()
    str_list = []
    index = 0
    while index <= len(string) - 2:
        st = string[index:index + 2]
        if st.isalpha():
            str_list.append(st)
        index += 1
    return str_list


def solution(str1, str2):
    str1_list = makeSplit(str1)
    str2_list = makeSplit(str2)

    dupli = set(str1_list) & set(str2_list) # 교집합
    union = set(str1_list) | set(str2_list) # 합집합

    # 교집합 요소가 집합 a, b에 몇개 있는지 각각 구한 후 그 중 최소값을 구하면 다중집합의 교집합 개수를 구할 수 있다
    dupli_count = sum([min(str1_list.count(i), str2_list.count(i)) for i in dupli])
    # 합집합 요소가 집합 a, b에 몇개 있는지 각각 구한 후 그 중 최대값을 구하면 다중집합의 합집합 개수를 구할 수 있다
    union_count = sum([max(str1_list.count(i), str2_list.count(i)) for i in union])
    if dupli_count == 0 and union_count == 0:
        answer = 65536
    else:
        answer = math.trunc((dupli_count / union_count) * 65536)

    return answer