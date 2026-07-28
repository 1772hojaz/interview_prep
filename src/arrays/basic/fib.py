#!/bin/python3

def fib(x):
    a = 0
    b = 1

    for i in range(x):
        print(a)
        a = b
        b = a + b


fib(10)    
