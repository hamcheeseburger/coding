input_list = input()

sum = ''
syn = []
for l in input_list:
    if l.isdigit():
        sum += l
    else:
        syn.append(int(sum))
        syn.append(l)
        sum = ''
syn.append(int(sum))
flag = True
while flag:
    flag = False
    for i in range(len(syn)):
        if syn[i] == '+':
            newNum = syn[i-1]+syn[i+1]
            del syn[i-1:i+2]
            syn.insert(i-1, newNum)
            flag = True
            break

answer = syn[0]
for i in range(2, len(syn)):
    if syn[i] != '-':
        answer -= syn[i]

print(answer)