# Python web-crawling exercises - user justify functions

'''
def p(x, y):
    result = print('The result of %s + %s is %s' %(x, y, x+y))
    #return result

p(3,478)


" Don't know how many values will be input from user : *x "
def p(*x):
    hap = 0
    for i in x:
        hap += i
    return("Your input values adding result is %s" %hap)

print(p(1,2,3))
print(p(2,4,6,8, 10, 12))


def p(a, b):
    if a > b :
        return (a-b)
    elif a < b :
        return (b-a)
    else:
        return(0)
    
print(p(50000, 50000))


def func(*x):
    a =[]
    for i in x:
        a.append(i)
    a.sort()
    return(a[-1])

print(func(1,5,23,78,924,65,32))


def func(*x):
    a = 0
    for i in x:
        a += i
    return(a)

print(func(2,45,63,74,902,305,1024))


def func(*x):
    a =[]
    for i in x:
        a.append(i)
    a.sort()
    b = a[-1] - a[0]
    return(b)

print(func(1,5,23,78,924,65,32))


import sys
print(sys.path)
sys.path.append("C:\\Users\\chois\\Desktop\\Jupyter codes\\Modules")
from Python_module_ex_1.m_1()


import sys
sys.path.append("C:\\Users\\chois\\Desktop\\Jupyter codes\\Modules")
print(sys.path)
from Python_module_ex_1 import m_1, m_2

print(m_1())
print(m_2())
print(m_3())
print(m_4())

'''
import sys
sys.path.append("C:\\Users\\chois\\Desktop\\Jupyter codes\\Modules")
print(sys.path)
import Python_module_ex_2
Python_module_ex_2.add(3,4)
Python_module_ex_2.sub(3,4)
Python_module_ex_2.mul(3,4)
Python_module_ex_2.div(3,4)