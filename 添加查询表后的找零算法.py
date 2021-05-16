def recDC(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        return 1
    elif knowResults[change - 1] > 0:
        return knowResults[change - 1]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change - 1] = minCoins
        return minCoins


print(recDC([1, 2, 5, 10, 20, 50], 85, [0]*85))