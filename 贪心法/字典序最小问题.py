def solve(s):
    if len(s) == 1:
        result = s
        return result
    S = list(s)
    Sprime = S[::-1]
    result = ''
    flag = True

    for i in range(len(s)):
        # 按照字典序比较s和s翻转后的字符串，s较小就从开头取出一个字符，放到结果中
        # 反之就从末尾追加到结果中
        if S[i] > Sprime[i]:
            flag = False
            break
        elif S[i] < Sprime[i]:
            break
    if flag:
        result += S[0]
        result += solve(s[1::])
    else:
        result += Sprime[0]
        result += solve(s[:-1])
    return result


if __name__ == '__main__':
    S = "ACDBCA"
    print(solve(S))
