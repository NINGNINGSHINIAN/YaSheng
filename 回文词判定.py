from pythonds.basic.deque import Deque


def palchecker(aString):
    charDeque = Deque()
    for ch in aString:
        charDeque.addRear(ch)
    
    stillEqual = True
    while charDeque.size() > 1 and stillEqual:
        stillEqual = charDeque.removeFront() == charDeque.removeRear()
        
    return stillEqual


print(palchecker('124321'))
