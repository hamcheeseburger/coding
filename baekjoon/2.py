def solution(log):
    runningtime = 0
    for i in range(0, len(log) - 1, 2):
        second = log[i + 1].split(":")
        first = log[i].split(":")

        hour = int(second[0]) - int(first[0])
        minute = int(second[1]) - int(first[1])
        running = hour * 60 + minute
        if running > 105:
            running = 105
        if running < 5:
            running = 0
        runningtime += running

    # print(runningtime)
    running_hour = runningtime//60
    running_minute = runningtime%60

    if running_hour < 10:
        running_hour = '0'+str(running_hour)
    else:
        running_hour = str(running_hour)

    if running_minute < 10:
        running_minute = '0'+str(running_minute)
    else:
        running_minute = str(running_minute)

    answer = running_hour + ':' + running_minute
    return answer