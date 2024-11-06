#최소공배수는 두 수의 곱 / 최대공약수로 구할 수 있다.


#최대공약수 구하는 함수
def commonDiv(n, m):
    listn = []
    listm = []
    for i in range(1, n+1):
        if n % i == 0:
            listn.append(i)

    for i in range(1, m+1):
        if m % i == 0 and i in listn:
            listm.append(i)

    return max(listm)


def commonMul(n, m):
    return n * m // commonDiv(n, m)


n, m = map(int, input().split())
print(commonMul(n, m))