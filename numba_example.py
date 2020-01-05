from numba import njit
import numpy as np
import random
from timeit import default_timer as timer
import matplotlib.pyplot as plt


to_plot=[]
plots=[]
num=0
@njit
def man(N):
 a=[[random.randrange(0,9) for i in range(N)] for j in range(N)]
 b=[[random.randrange(0,9) for i in range(N)] for j in range(N)]
 result=[[0 for i in range(N)] for j in range(N)] # iterate through rows of X
 for i in range(len(a)):
   # iterate through columns of Y
   for j in range(len(b[0])):
       # iterate through rows of Y
       for k in range(len(b)):
           result[i][j]+=a[i][k] * b[k][j]
while num !=500:
 t=timer()
 man(num)
 e=timer()-t
 to_plot.append(e)
 num+=10
 plots.append(num)
print(to_plot)
plt.style.use("seaborn-darkgrid")
plt.plot(plots[1:],to_plot[1:],linestyle='dashed', linewidth = 1,marker='x', markerfacecolor='yellow', markersize=0.5)
plt.show()
