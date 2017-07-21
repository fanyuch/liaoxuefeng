#筛选回数
def is_plaindrom(n):
    mList = list()
    while n > 0:
        tmp = n % 10
        mList.append(tmp)
        n = n // 10
    n = 0
    while n <len(mList) / 2:
        if mList[n] != mList[len(mList) - n -1]:
            return False
        else:
            n += 1
    return True



for y in filter(is_plaindrom, [x for x in range(1000)]):
    print(y)

