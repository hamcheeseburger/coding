# 프로그래머스 기능개발(210630)
# https://programmers.co.kr/learn/courses/30/lessons/42586

import math
import numpy as np


def solution(progresses, speeds):
    answer = []
    while True:
        if len(progresses) == 0 and len(speeds) == 0:
            break

        progresses = np.array(progresses)
        copy_speeds = np.array(speeds)

        rest_of_first = 100 - progresses[0]

        release_term = math.ceil(rest_of_first / speeds[0])

        copy_speeds = copy_speeds * release_term

        progresses += copy_speeds

        count = 0
        for ele in progresses:
            if ele < 100:
                break
            count += 1

        progresses = list(progresses)

        del progresses[0:count]
        del speeds[0:count]

        answer.append(count)
    return answer