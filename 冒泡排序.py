def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i + 1], alist[i] = alist[i], alist[i + 1]


alist = [3, 5, -1, 2, 6]
print(alist)
bubbleSort(alist)
print(alist)