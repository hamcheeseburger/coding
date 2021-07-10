def jumpCursor(cursor, jump, length):
    cursor = cursor + jump
    if cursor < 0:
        cursor += length

    if cursor >= length:
        cursor -= length

    return cursor


def solution(name):
    name = list(name)
    a_indexs = list(filter(lambda x: name[x] == 'A', range(len(name))))

    visited = [0 for i in range(len(name))]

    for a_index in a_indexs:
        visited[a_index] = 1

    cursor = 0
    answer = 0
    jump = 0
    while True:
        answer += jump

        if visited[cursor] == 0:
            a_minus = ord(name[cursor]) - ord('A')
            z_minus = ord('Z') - ord(name[cursor]) + 1
            answer += min(a_minus, z_minus)
            visited[cursor] = 1

        # 방문하지 않은 것중 제일 가까운 것 찾기
        not_visited_indexs = list(filter(lambda x: visited[x] == 0, range(len(visited))))

        if len(not_visited_indexs) == 0:
            break

        min_jump = 9999
        next_cursor = 0
        for index in not_visited_indexs:
            # 정순, 역순으로 이동할 때 더 적은 수 찾기
            gap = abs(cursor - index)
            back_gap = len(name) - gap
            local_min = min(gap, back_gap)
            if min_jump > local_min:
                min_jump = local_min
                next_cursor = index

        jump = min_jump
        cursor = next_cursor

    return answer