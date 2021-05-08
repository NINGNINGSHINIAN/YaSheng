def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentValue


def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)

        print("After increment of size", sublistCount, "The list is", alist)
        sublistCount = sublistCount // 2


alist = [3, 5, -1, 2, 6]
print(alist)
shellSort(alist)
print(alist)