def solution(priorities, location):
    # enumerate는 리스트의 순서와 값을 전달함
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        # 현재 남아있는 작업중 더 우선순위가 높은 것이 있다면 true, 없다면 false
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
