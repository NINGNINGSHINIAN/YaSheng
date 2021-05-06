from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    # 首先，创建空栈opStack用于暂存操作符，空表postfixList用于保存后缀表达式
    opStack = Stack()
    postfixList = []
    # 将中缀表达式转换为单词（token）列表
    tokenList = infixexpr.split()

    for token in tokenList:
        # 如果单词是操作数，则直接添加到后缀表达式列表的末尾
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
                or token in "0123456789":
            postfixList.append(token)
        # 如果单词是左括号“(”，则压入opStack栈顶
        elif token == '(':
            opStack.push(token)
        # 如果单词是右括号“)”，则反复弹出opStack栈顶操作符，加入到输出列表末尾，直到碰到左括号
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        # 如果单词是操作符“ * / +-”，则压入opStack栈顶
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
    # 中缀表达式单词列表扫描结束后，把opStack栈中的所有剩余操作符依次弹出，添加到输出列表末尾
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def doMath(op, operand1, operand2):
    if op == '+':
        return operand1 + operand2
    elif op == '-':
        return operand1 - operand2
    elif op == '*':
        return operand1 * operand2
    else:
        return operand1 / operand2


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def main():
    infixExpr = "( 3 - 2 )"
    postfixExpr = infixToPostfix(infixExpr)
    print("后缀表达式%s的值是: " % postfixExpr + str(postfixEval(postfixExpr)) + '!')


if __name__ == '__main__':
    main()
    # prec = {}
    # prec["*"] = 3
    # prec["/"] = 3
    # prec['+'] = 2
    # prec['-'] = 2
    # prec['('] = 1
    # print("".join(prec))
