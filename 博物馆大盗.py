treasure = [None, {'w': 2, 'v': 3},
            {'w': 3, 'v': 4},
            {'w': 4, 'v': 8},
            {'w': 7, 'v': 8},
            {'w': 5, 'v': 5}]

max_weight = 20
m = {(i, w): 0 for i in range(len(treasure))
     for w in range(max_weight + 1)}

for i in range(1, len(treasure)):
    for w in range(1, max_weight + 1):
        if treasure[i]['w'] > w:
            m[(i, w)] = m[(i - 1, w)]
        else:
            m[(i, w)] = max(m[(i - 1, w)],
                            m[(i - 1, w - treasure[i]['w'])] + treasure[i]['v'])

print(m[(len(treasure) - 1, max_weight)])
g = [x * x for x in range(10)]
print(g)
