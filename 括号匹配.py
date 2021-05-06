from pythonds.basic.stack import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return "括号是匹配的！"
    else:
        return "括号不匹配，请检查！"


def matches(top, symbol):
    opens = '([{'
    closes = ')]}'
    if opens.index(top) == closes.index(symbol):
        return True


def main():
    print(parChecker("(((())))"))
    print(parChecker("(((()))"))
    print(parChecker("[{}]()[({})]"))
    print(parChecker("[{}]()[{})]"))


if __name__ == '__main__':
    main()
print(5 / 2)
