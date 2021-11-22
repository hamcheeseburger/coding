def solution(arr):
    dic = {}
    dic[1] = 0
    dic[2] = 0
    dic[3] = 0
    for ele in arr:
        dic[ele] += 1

    max_val = 0
    for i in range(1, 4):
        if max_val < dic[i]:
            max_val = dic[i]

    answer = []
    for i in range(1, 4):
        answer.append(max_val - dic[i])

    return answer