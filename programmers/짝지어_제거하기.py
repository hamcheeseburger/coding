# 프로그래머스 짝지어 제거하기(210629)
# https://programmers.co.kr/learn/courses/30/lessons/12973

# def solution(s):
#     answer = -1
#     condition = True
#
#     s_list = list(s)
#     while condition:
#         for i in range(len(s_list)):
#             if i != len(s_list) - 1 and s_list[i] == s_list[i + 1]:
#                 del s_list[i:i + 2]
#                 condition = False
#                 break
#
#         if condition == False:
#             condition = True
#         else:
#             condition = False
#
#     if len(s_list) == 0:
#         return 1
#     return 0

def checkPair(s):
    stack = []
    for ele in s:
        # 스택이 비워져 있다면 해당 원소 삽입
        if len(stack) == 0:
            stack.append(ele)
        #  현재 원소와 스택의 마지막 원소가 같다면 스택에서 해당 원소 제거
        elif stack[len(stack)-1] == ele:
            stack.pop()
        #  현재 원소와 스택의 마지막 원소가 다르다면 현재 원소 삽입
        else:
            stack.append(ele)
    if len(stack) == 0:
        return 1
    return 0

def solution(s):
    return checkPair(s)

print(solution("bbbbb"))