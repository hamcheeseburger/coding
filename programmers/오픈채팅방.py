# 프로그래머스 오픈채팅방(210702)
# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    nickname = {}
    answer = []
    for cmd in record:
        cmd_list = cmd.split()

        if len(cmd_list) == 3:
            # print(cmd_list)
            nickname[cmd_list[1]] = cmd_list[2]

    for cmd in record:
        cmd_list = cmd.split()
        if cmd_list[0] == 'Enter':
            s = nickname[cmd_list[1]] + '님이 들어왔습니다.'
            answer.append(s)
        if cmd_list[0] == 'Leave':
            s = nickname[cmd_list[1]] + '님이 나갔습니다.'
            answer.append(s)

    return answer