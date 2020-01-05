import time,random
import matplotlib.pyplot as plt
import numpy as np
list=[]
nptime=[]
nparrtime=[]
pytime=[]
N=0
while N!=500:
 B =np.random.randint(10,size=(N,N))
 A=np.random.randint(10,size=(N,N))
 t=time.time()
 np.dot(A,B)
 npt=str(time.time()-t)[:6]
 nptime.append(float(npt))
 X =[[random.randrange(0,9) for i in range(N)] for j in range(N)]
 Y =[[random.randrange(0,9) for i in range(N)] for j in range(N)]
 v=time.time()
 nptm=str(time.time()-v)[:6]
 nparrtime.append(float(nptm))
 result = [[0 for i in range(N)] for j in range(N)]
 # iterate through rows of X
 r=time.time()
 for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
 pyt=str(abs(time.time())-r)[:6]
 pytime.append(pyt)
 N+=10
 list.append(N)
print(nptime)
print(nparrtime)
print(pytime)
plt.style.use("seaborn-darkgrid")
plt.title("Comparing the time taken to multiply matrices")
plt.plot(list[1:],nptime[1:], label="time taken by numpy+numpy.array")
plt.plot(list[1:],nparrtime[1:], label="time taken by numpy+normal list")
plt.plot(list[1:],pytime[1:], label="time taken by a norml for loop")
plt.legend()
plt.tight_layout()
plt.xlabel("Order of the matrix")
plt.ylabel("Time taken")
plt.show()
plt.savefig("task.png")
