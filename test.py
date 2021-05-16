# def fib(max):
#     a, b = 1, 1
#     while a < max:
#         yield a
#         a, b = b, a + b
#
#
# for n in fib(15):
#     print(n)
#
# m = fib(13)
# print(m)
# print(m.__next__())
# print(m.__next__())
# print(m.__next__())
# print(m.__next__())

def yanghui_triangle():
    L = [1]
    while True:
        yield L
        # list(range(a,a))的输出为空
        L = [1] + [L[i - 1] + L[i] for i in range(1, len(L))] + [1]


# if __name__ == ' __main__':
n = 0
for i in yanghui_triangle():
    print(i)
    n += 1
    if n > 10:
        break
