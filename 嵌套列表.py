# BinaryTree函数构造一个很简单的列表，它仅有一个根节点和两个作为子节点的空列表
def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == '__main__':
    r = BinaryTree(3)
    print(insertLeft(r, 4))
    print(insertLeft(r, 5))
    print(insertRight(r, 6))
    print(insertRight(r, 7))
    l = getLeftChild(r)
    print(l)
