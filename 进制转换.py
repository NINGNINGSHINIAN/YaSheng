from pythonds.basic.stack import Stack


def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'
    newString = ''

    remStack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    while not remStack.isEmpty():
        newString = newString + digits[remStack.pop()]
    return newString


def main():
    print(baseConverter(256, 2))
    print(baseConverter(256, 16))


if __name__ == '__main__':
    main()
