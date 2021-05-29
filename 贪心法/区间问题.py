def solve(s, t):
    # 使用zip函数由两个列表生成字典
    dictionary = dict(zip(t, s))
    # 根据任务结束时间对其排序
    dictionary = dict(sorted(dictionary.items(), key=lambda x: x[0]))
    array = list(dictionary.keys())
    currentT = array[0]
    print('选中了开始时间为 %d 的任务' % dictionary[array[0]])
    count = 1

    for i in range(1, len(array)):
        # 在可选的工作中，每次都选取结束时间最早的工作
        if dictionary[array[i]] > currentT:
            print('选中了开始时间为 %d 的任务' % dictionary[array[i]])
            currentT = array[i]
            count += 1

    return count


if __name__ == '__main__':
    # 输入任务数目和开始结束的时间
    n = 5
    s = [1, 2, 4, 6, 8]
    t = [6, 5, 7, 9, 10]

    print(solve(s, t))
