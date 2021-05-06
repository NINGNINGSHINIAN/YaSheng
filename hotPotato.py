from pythonds.basic.queue import Queue


def hotPotato(numberlist, num):
    simqueue = Queue()
    for number in numberlist:
        simqueue.enqueue(number)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato([x + 1 for x in range(10)], 1))
