# 백준 1182 recursion으로 작성

def recursion(num_list, startIndex, purposeCounts, pickedCounts, purposeNum):
    picked.append(num_list[startIndex])
    if pickedCounts == purposeCounts - 1:
        # print(picked)
        count = 0
        if sum(picked) == purposeNum:
            count = 1
        picked.remove(num_list[startIndex])
        return count

    local_count = 0
    for i in range(startIndex + 1, len(num_list)):
        local_count += recursion(num_list, i, purposeCounts, pickedCounts + 1, total)

    picked.remove(num_list[startIndex])
    return local_count


N, total = map(int, input().split())
num_list = list(map(int, input().split()))

picked = []

total_count = 0
for j in range(1, len(num_list)+1):
    for i in range(len(num_list)):
        total_count += recursion(num_list, i, j, 0, total)

print(total_count)