def selectionSort(alist):
    for fillSlot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillSlot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[fillSlot], alist[positionOfMax] = alist[positionOfMax], alist[fillSlot]


alist = [3, 5, -1, 2, 6]
print(alist)
selectionSort(alist)
print(alist)
