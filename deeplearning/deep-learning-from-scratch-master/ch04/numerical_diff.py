# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

t1 = numerical_diff(function_tmp1, 3.0)
t2 = numerical_diff(function_tmp2, 4.0)

print("t1:"+str(t1) + " t2:"+str(t2))