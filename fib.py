#!/usr/bin/python

def gfib(f):
    a = b = 1
    for x in range(f):
        yield a
        a,b = b,a+b

def rfib(f):
    a = b = 1
    fib = []
    for x in range(f):
        fib.append(a)
        a, b = b, a+b
    return fib

#for x in gfib(100000):
#    print(x, " ")
x = rfib(10000000)
