

size = int(input())
num_list = list(map(int, input().split()))

# print(num_list)

# max_val = num_list[0]
# for i in range(size):
#     local_max = num_list[i]
#     tmp = 0
#     for j in range(i, size):
#         tmp += num_list[j]
#         if local_max < tmp:
#             local_max = tmp
#     if max_val < local_max:
#         max_val = local_max
#
# print(max_val)
memory = [[] for _ in range(size+1)]
memory[1] = num_list
max_val = num_list[0]
for group in range(2, size+1):
    for i in range(len(memory[group-1])-1):
        val = memory[group-1][i] + memory[1][i+group-1]
        memory[group].append(val)
        if max_val < val:
            max_val = val

# print(memory)
print(max_val)