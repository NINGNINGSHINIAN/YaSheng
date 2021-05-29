def solve(R, X):
    X = sorted(X)
    mark = [0] * len(X)
    i = 0

    while i < len(X):
        s = X[i]
        i = i + 1
        while i < len(X) and X[i] <= s + R:
            i += 1
        p = X[i - 1]
        mark[i - 1] = 1
        while i < len(X) and X[i] <= p + R:
            i += 1

    return mark


if __name__ == '__main__':
    R = 10
    X = [1, 7, 15, 20, 30, 50]
    print(solve(R, X))

