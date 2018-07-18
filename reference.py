import math
import pandas
from zekenetpy import ZekeNet
# a = 5 # int
# a = 5. # float
# a = "5" # string
#
# def f(x):
#     return math.pow(x,2) + 4
#
# def g(x):
#     return 3*x + 1
#
# def der_f(f,x):
#     h = .00001
#     y1 = f(x)
#     y2 = f(x+h)
#     d = (y2-y1)/h
#     return d
#
# print f(5)
#
# print der_f(f, 3)
# print der_f(g, 3)

ser = pandas.Series([1,2,3,4,5])
print ser

ser = ser / 3.
this_in = pandas.Series([3.])
nnet = ZekeNet(1,1)
nnet.set_inputs(this_in)
nnet.activate()




