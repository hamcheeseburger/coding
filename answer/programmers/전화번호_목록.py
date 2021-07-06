# 프로그래머스 전화번호 목록(210706)
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            # 해당 문자열의 문자 하나하나를 해시맵에 있는 요소와 비교
            # ['12', '12345']라면 '12345'가 number가 되고 temp가 '12'가 되는 시점에 해시맵에 있는 '12'라는 문자가 검색될것
            if temp in hash_map and temp != phone_number:
                print("in" + temp)
                answer = False
    return answer