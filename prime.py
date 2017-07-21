# -*- coding : utf-8 -*-
#求所有素数，无限序列

#生成一个从2开始的自然数序列，直接生成器
def OddList():
    n = 1
    while True:
        n += 1
        yield n

#定义删选函数
#首先理解一下filter()这个内建函数，他接受一个函数 和 一个序列，并且，这个函数接受序列的每一个元素作为参数传入函数，迭代一遍
#所以，只要是filter()括号内的函数，就一定有一个参数：序列的一个元素。
#由于multifilter是被filter()包含的，所以multerfilter中有一个参数是序列的元素，一定会传进来的，但是由于无法表示，所以用匿名

#firstNum是新序列的第一个元素，element是序列的每一个元素，这个参数是再filter()调用的时候，filter给传进来的，不用写在参数位置
def MultiFilter(firstNum):
    return lambda element: element % firstNum > 0   #如果列表元素 能够整除指定倍数，返回False, 在builtin-filter中被过滤掉，反之保留


#无限迭代奇数生成器，在每一个迭代中，生成一个新的序列（生成器），生成新序列的过程又是一个迭代过程，在这个过程中把元素n的倍数过滤掉
def PrimeList(maxNum):
    mainList = OddList()
    firstElement = next(OddList())    #curentElement 标签始终指向当前元素，作为倍数参与筛选
    yield firstElement
    while firstElement < maxNum:
        mainList = filter(MultiFilter(firstElement), mainList)     ##mainList 标签始终指向主生成器，用生成器OddList()初始化
        firstElement = next(mainList)             #每次只取新序列的一个元素
        yield firstElement

if __name__ == '__main__':
    for x in PrimeList(1000):
        print(x)

