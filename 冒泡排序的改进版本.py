def shortBubbleSort(alist):
    passnum = len(alist) - 1
    exchange = True
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i + 1], alist[i] = alist[i], alist[i + 1]
        passnum -= 1


alist = [3, 5, -1, 2, 6]
print(alist)
shortBubbleSort(alist)
print(alist)