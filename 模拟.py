from pythonds.basic.queue import Queue

import random


class Printer:
    def __init__(self, ppm):  # 其中ppm为打印机打印速度
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.busy():
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining == 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    # def getStamp(self):
    #     return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp


def newPrinterTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagePerMinute):
    labprinter = Printer(pagePerMinute)
    printerQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        # 如果有随机生成的打印任务进来，就把打印任务开始的时间记下来
        if newPrinterTask():
            task = Task(currentSecond)
            printerQueue.enqueue(task)
        # 如果打印机空闲且此时打印任务列表中有任务，
        if not labprinter.busy() and not printerQueue.isEmpty():
            nexttask = printerQueue.dequeue()
            waitingTimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printerQueue.size()))
    return averageWait


wait = []
for i in range(10):
    wait.append(simulation(100000, 5))
print(sum(wait) / 10)
