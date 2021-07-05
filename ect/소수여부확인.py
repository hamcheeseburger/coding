
def isPrime(n):
    if n <= 1: # 0과 1은 소수가 아니므로
        return False

    # 해당 숫자의 제곱근 + 1까지의 수가 약수라면 소수가 아닌 수,
    # 그에 해당하는 약수가 없다면 소수
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(isPrime(11))
