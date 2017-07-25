# -*- coding: utf-8 -*-
import chardet
import random
import os
from collections import Iterator

print('中文')
print(ord('中'))
print(chr(20013))
print('\u4e2d\u6587')

#编码是 对象到机器码的过程。如：'abc'到 011001的过程；
#解码是 机器码到对象的过程。如：011001010 到'中'的过程；
#所有字符串都会编码成字节码，或叫做机器码，因为计算机只认0，1。机器码就是0，1的编码
print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#python中  机器码用类型byte类型标识，也称为字节码
print(chardet.detect(b'abc')['encoding'])
print(chardet.detect(b'\xe4\xb8\xad\xe6\x96\x87')['encoding'])
#print(chardet.detect('adc'))  #这样就会报错，因为detect函数接受一个byte string，可翻译为字节串，而不是字符串，字节串就是机器码（字节码）

#格式化
print('hello %s,my name is %s'%('evry', 'fanyuchen'))
r = (85-72)/72
print('rase %.2f'%r)


random.random

mList1 = list([x for x in range(10)])
mList2 = list(range(1,10))
#元组不变指的是 元组元素指向不变
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[2][2])

#字符串整数初始化
# birth = input('input birth :...')
# if int(birth) < 2000:
#     print('00后')
# else:
#     print('00钱')

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello, %s'% name)

my_list = list('bart')
print(my_list)
if 'ann' in L:
    print('yes')

t1 = (1, 2, 3)
t2 = (1, [2, 3])
mDic = {}
mDic['t1'] = t1
mDic['t2'] = t2


print(mDic)
pass

#break与continue的区别

x = str((hex(23)))
print(x)

def fun(name, sex):
    print('name is %s'%name)
    print('sex is %s\n'%sex)

fun('fan', 'male')
fun('male', 'fan')

fun(name = 'fan', sex = 'male')
#参数名参数
fun(sex = 'male', name = 'fan')

#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:3])
print( (0, 1, 2, 3, 4, 5)[:-2])
#string也是可迭代对象
myStr = str('Michael')
for x in myStr:
    print(x)

#列表生成式
print([x*y for x in range(10) for y in range(10)])
pass
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k,v in d.items():
    print('key%s = value%s'%(k, v))

print([k+'='+v for k,v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']

print([s.lower() for s in L])


#显示文件列表常用
print([d for d in os.listdir("c:\\")])
for d in os.listdir('c:\\'):
    print(d+'\n')

#生成式中包含if判断
L = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L if isinstance(s, str)])
pass

#生成器与生成式的区别，生成式是所有数据，生成器是算法
print("生成器与生成式的区别，生成式是所有数据，生成器是算法")
print((x*x for x in range(10))) #无法直接打印，需要迭代才能看出来

#迭代生成器
for x in (x*x for x in range(10)):
    print(x)

#斐波那契数列的生成器表示
print("斐波那契数列的生成器表示")
def Fibonacci(imax):
    n, a, b = 0, 0, 1
    while n < imax:
        yield b                      #生成器的执行顺序， 遇到"生成"从当前函数中返回， 下次迭代是，衔接上一次"生成"之后的语句执行，循环往复
        a, b = b, a + b
        n += 1
    return None

for x in Fibonacci(10):
    print(x)

print("杨辉三角生成器")
def get_pascal_triangle2(n):
    list = [1]
    while n > 0:
        yield list
        list = [1] + [x + y for x, y in zip(list[:], list[1:])] + [1]
        n -= 1
    return

for t in get_pascal_triangle2(10):
    print(t)
    #n = n + 1
    # if n == 10:
    #     break

#杨辉三角另一种方法
def yhTriangle(n):
    l, index = [1], 0
    while index < n:
        yield l
        l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
        index += 1

for x in yhTriangle(10):  #加上yield的函数变成生成器了，所以也是可以迭代的对象
    print(x)


#迭代器
print(isinstance([], Iterator))

m_list = [x for x in range(1, 101)]

p = sum(m_list)
print(m_list)
from functools import reduce
def prod(x1, x2):
    return x1 + x2
p = reduce(prod, m_list)
print(p)
#组装
def fun(s1, s2):
    return s1*10 + s2

print(reduce(lambda x, y:x*10 + y, [1, 3, 5, 7, 9]))

#str 转换为 int
def char2int(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
map(char2int, [1, 3, 5, 7, 9])


#生成数字列表
m_list = []
for x in map(str, [x for x in range(1, 10)]):
    m_list.append(x)
m_list[5] = '.'

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('12300.456'))
# for x in m_list:
#      print(x + ' :type of x is %s'%type(x))

#filter   过滤掉奇数
print(list(filter(lambda x: x % 2 == 0, [x for x in range(20)])))

#filter
print(list(filter(lambda x : x % 2 > 0, [x for x in range(10)])))
pass

#求所有素数，无限序列
# def geneList():
#     n = 1
#     while True:
#         n += 2
#         yield n
#
# def myFilter(n):
#     return lambda x : x % n > 0
#
# def primeFilter():
#     yield 2
#     mGen = geneList()
#     while True:
#         n = next(mGen)
#         yield n
#         mGen = filter(myFilter(n), mGen)
#
#
# for x in primeFilter():
#     if x <1000:
#         print(x)
#     else:
#         break


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


#sorted()     #自定义函数可以，匿名函数也可以
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(L, key=lambda t: t[1]))  #key函数的执行流程是：先把key应用再列表上，再把排序应用再列表上

def Keyfun(L):
    return L[1]

print(sorted(L, key=Keyfun))


#闭包，要理解闭包，只需要单步跟进

# def count():
#     mList = []
#     for i in range(4):
#         def fun():
#             return i*i
#         mList.append(fun)
#     return mList
#
# f1, f2, f3, f4 = count()
#
# f1()
# f2()
# f3()
# f4()


#闭包  的环境变量，自由变量
s = 'string in blobal'
num = 99

def numFunc(a, b):
    num = 100
    num2 = 200
    num3 = 300
    print('print s in numbunc', s)

    def addfunc(a, b):
        s = 'string in addfunc'
        x = num
        y = num3
        print('print s in addFunc', s)

    return addfunc



print(dir(numFunc))
print('numFunc', numFunc.__closure__)
print('addfunc', numFunc(1, 3).__closure__)
for x in numFunc(1, 3).__closure__:
    print(x)
    pass





# def line_conf():
#     def line(x):
#         return 2 * x + 1
#
#     print(line(5))  # within the scope
#
#
# line_conf()
# print(line(5))  # out of the scope

def line_conf():
    b = 15

    def line(x):
        return 2 * x + b

    return line  # return a function object


b = 5
my_line = line_conf()
print(my_line.__closure__[0].cell_contents)
print(type(my_line.__closure__))
pass


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(type(f1.__closure__))
pass

#元组也可以迭代
x = tuple([1, 2, 3])

for y in x:
    print(y)



#装饰器
def log(func):
    def wrapper():
        print('call %s():' % func.__name__)
        return func()                 #返回函数名字和返回函数调用 是不一样的

    return wrapper

@log
def m_fun():
    print('hello world')

m_fun()

# class student(object):
#     __slots__ = ('name', 'sex')
#
# s = student()
# s.name = 'fan'
# s.sex = 'male'
# s.score = 0

class student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter                   #setter是  porperty的内建函数
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s = student()
# s.birth = 10
# print(s.birth)


#@property 的引用
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resulation(self):
        return self._height * self._width

    @resulation.getter
    def resulation(self):
        return self._height * self._width

sc = Screen()
sc.height = 9
print(sc.height)

sc.width = 10
print(sc.width)

print(sc.resulation)











