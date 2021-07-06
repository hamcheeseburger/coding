# 프로그래머스 전화번호 목록(210706)
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    # 숫자로 된 문자열을 sort()하면
    # ["119", "97674223", "1195524421"] => 	['119', '1195524421', '97674223']
    # 비슷한 문자열끼리 모이게 된다.
    phone_book.sort()

    # 비슷한 문자열끼리 모이므로 양 옆에 있는 문자끼리 비교하면 된다.
    for i in range(len(phone_book) - 1):
        a_len = len(phone_book[i])
        b_len = len(phone_book[i+1])
        if phone_book[i] == phone_book[i+1][:a_len] or phone_book[i+1] == phone_book[i][:b_len]:
            return False
    return True