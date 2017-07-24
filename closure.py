# -*- coding : utf-8 -*-

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
    return f

x = None

f1 = count()
x = f1()

pass