from 节点 import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = self.search(item)
        if not found:
            print("列表中无此元素！")
        else:
            print("列表中有此元素！正在删除")
            found = False
            while not found:
                if current.getData() == item:
                    found = True
                else:
                    previous = current
                    current = current.getNext()
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())


myList = UnorderedList()
print(myList.isEmpty())
myList.add(31)
myList.add(77)
myList.add(91)
myList.add(100)
print(myList.isEmpty())
print(myList.length())
myList.remove(8)
myList.remove(100)
