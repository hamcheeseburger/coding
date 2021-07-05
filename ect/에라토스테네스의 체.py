# 에라토스테네스의 체를 이용하여 n 이하의 약수를 찾아보자.

# n 이하의 약수 찾기!

def prime_list(n):
    # n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True: # i가 소수인 경우
            for j in range(i+i, n, i): # 소수의 배수는 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]