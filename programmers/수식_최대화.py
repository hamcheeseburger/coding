# 프로그래머스 수식 최대화(210705)
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re
from itertools import permutations
import copy


def solution(expression):
    # 숫자 뽑아내기
    numbers = re.findall("\d+", expression)

    # 연산자 뽑아내기
    expressions = set()
    order_expressions = []
    for i in range(len(expression)):
        if not expression[i].isdigit():
            expressions.add(expression[i])
            order_expressions.append(expression[i])
    expressions = list(expressions)

    # 연산자 우선순위 경우의 수 구하기
    expressions_priority = list(permutations(expressions, len(expressions)))

    # 원본 배열 남겨놓기
    numbers_copy = copy.deepcopy(numbers)
    order_expressions_copy = copy.deepcopy(order_expressions)

    result = []
    for express in expressions_priority:
        # 초기화
        numbers = copy.deepcopy(numbers_copy)
        order_expressions = copy.deepcopy(order_expressions_copy)
        for i in range(len(expressions)):
            # 해당 연산자를 가지는 index 구하기
            express_index = list(filter(lambda x: order_expressions[x] == express[i], range(len(order_expressions))))

            for j, index in enumerate(express_index):
                # 삭제하면 원소들이 앞으로 밀리기 때문에 index를 j만큼 앞으로 옮기기
                index = index - j

                # 해당 연산 수행
                local_num = eval(numbers[index] + order_expressions[index] + numbers[index + 1])

                # 연산식 삭제
                del numbers[index]
                del order_expressions[index]

                # 연산결과 삽입
                numbers[index] = str(local_num)
        result.append(abs(int(numbers[0])))

    return max(result)

solution("100-200*300-500+20")