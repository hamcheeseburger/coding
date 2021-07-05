# 프로그래머스 가장큰수 (210705)
# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    num_str = [str(num) for num in numbers]

    num_str.sort(key=lambda x: x * 4, reverse=True)

    answer = "".join(num_str)

    if answer[0] == "0":
        return "0"

    return answer