import collections
import itertools


def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)
        # print(order_combinations)
        # most_common()은 원소가 많이 나온 순으로 정렬을 해준다. (해당 코스요리에서 제일 많이 나온 조합을 알 수 있음)
        most_ordered = collections.Counter(order_combinations).most_common()

        # most_ordered[0][1]은 제일 큰 값. 제일 큰 값을 가지고 그 값이 2 이상인 조합 찾기
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]