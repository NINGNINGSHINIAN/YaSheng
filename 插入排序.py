def insertionSort(alist):
    for index in range(1, len(alist)):
        currentValue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentValue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentValue


alist = [3, 5, -1, 2, 6]
print(alist)
insertionSort(alist)
print(alist)
