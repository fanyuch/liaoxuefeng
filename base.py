# -*- coding: utf-8 -*-
import chardet
import random
import os

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

for x in yhTriangle(10):
    print(x)