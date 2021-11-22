# 회의실 배정

size = int(input())

input_list = []
for i in range(size):
    start, end = map(int, input().split())
    input_list.append((start, end))

input_list = sorted(input_list, key=lambda x:(x[1], x[0]))

# 빨리 끝나는 것부터 select (greedy)
memory = [input_list[0]]
for i in range(1, len(input_list)):
    m_start = memory[len(memory)-1][0]
    m_end = memory[len(memory)-1][1]
    if m_end <= input_list[i][0]:
        memory.append(input_list[i])

# print(memory)
print(len(memory))
