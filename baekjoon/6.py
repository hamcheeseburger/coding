import re


def solution(time, plans):
    value = {}
    fri_in = "9:30"

    for plan in plans:
        leave_num = re.findall(r'\d+', plan[1])[0]
        arrive_num = re.findall(r'\d+', plan[2])[0]
        leave_num = int(leave_num)
        arrive_num = int(arrive_num)

        # print(arrive_num)
        vac = 0
        if plan[1].find("PM") != -1:
            leave_num += 12
        elif leave_num == 12:  # 오전 12시(자정)
            leave_num = 0
        if plan[2].find("PM") != -1:
            arrive_num += 12
        elif arrive_num == 12:  # 오전 12시(자정)
            arrive_num = 0

        if leave_num <= 9:  # 금요일 출근시간 보다 적은 경우
            leave_num = fri_in
        else:
            leave_num = str(leave_num) + ":00"

        leave_splited = leave_num.split(":")
        leave_hour = int(leave_splited[0])
        leave_min = int(leave_splited[1])
        if leave_hour < 18:  # 금요일 퇴근시간보다 적은 경우
            if leave_min == 30:
                vac += 0.5
                leave_hour += 1
            vac += (18 - leave_hour)

        # 이경우에는 30분 단위가 안나오니까 숫자로 처리

        if arrive_num > 18:  # 월요일 퇴근시간 보다 큰 경우
            arrive_num = 18

        if arrive_num > 13:  # 월요일 출근시간 보다 큰 경우
            vac += (arrive_num - 13)
        value[plan[0]] = vac

    print(value)

    result = []
    for key in value.keys():
        if time - value[key] >= 0:
            result.append(key)
            time -= value[key]

    if len(result) == 0:
        return ''

    answer = result[len(result) - 1]
    return answer

print(solution(8.5, [["홍콩", "10AM", "12AM"]]))