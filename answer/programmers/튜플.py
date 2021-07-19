
import re
from collections import Counter


def solution(s):
    s = Counter(re.findall('\d+', s))
    # 제일 많은 순으로 정렬 (문제를 잘 살펴보니 요소가 많은 순으로 리스트가 나열되어 있었음)
    answer_list = sorted(s.items(), key=lambda x: x[1], reverse=True)

    answer = []
    for ele in answer_list:
        answer.append(int(ele[0]))

    return answer

