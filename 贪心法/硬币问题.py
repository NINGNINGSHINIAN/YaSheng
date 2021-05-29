def solve(A, C, value):
    ans = 0

    for i in range(5, -1, -1):
        t = min(A // value[i], C[i])
        A -= t * value[i]
        ans += t
    print(ans)


if __name__ == '__main__':
    # 硬币的面值
    value = (1, 5, 10, 50, 100, 500)

    # 输入各面值对应的硬币数量，要找的余额
    C = [3, 2, 1, 3, 0, 2]
    A = 620
    solve(A, C, value)
