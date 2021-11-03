def checkMatch(ele, poped):
    if ele == ']' and poped == '[':
        return 3
    if ele == ')' and poped == '(':
        return 2
    return 0

def sumNum(stack):
    index = 0
    num = 0
    for i in range(len(stack)-1):
        if stack[i].isdigit() and stack[i+1].isdigit():
            index = i
            num = int(stack[i]) + int(stack[i+1])
            break
    if num != 0:
        stack[index] = str(num)
        del stack[index+1]

input_list = list(input())
stack = []
for ele in input_list:
    if not stack: # 스택이 비어있다면
        stack.append(ele)
        continue

    first = stack.pop()
    if first.isdigit():
        if stack:
            second = stack.pop()
            if not checkMatch(ele, second):
                stack.append(second)
                stack.append(first)
                stack.append(ele)
            else:
                val = int(first) * checkMatch(ele, second)
                stack.append(str(val))
        else:
            stack.append(first)
            stack.append(ele)

    else:
        if not checkMatch(ele, first):
            stack.append(first)
            stack.append(ele)
        else:
            stack.append(str(checkMatch(ele, first)))

    sumNum(stack)
#     print(stack)

sum = 0
for s in stack:
    if not s.isdigit():
        sum = 0
        break
    sum += int(s)

print(sum)





