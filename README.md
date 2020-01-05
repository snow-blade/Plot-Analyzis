# Plot-Analyzis
A Repo which questions deep flaws of our oh so loved python with plots and analyzis in a readme<br><br>
I stopped the computation at a (500,500) matrix because my gpu is really old but instead of going from 10 to 100 to 1000...i instead advanced 10 by ten (x+10,y+10) and got a good enough data set.<br>
You can find my hardware info in the `hardare_info.txt` file.<br>
To install all the needed packages write `$ pip install -r requirements.txt`<br>
First let's start with a simple image of the obtained graph:
![Original one](/img/task.png "First graph") 
You might certainly Be asking yourself these questions.

### 1. Why is the python code with a for loop so slow?:
<br>
First, let's make a simple comparison between python and a 'faster' language, let's take for example c,
<br>
Python is a higher level language than C, which means it abstracts the details of the computer from you - memory management, pointers, etc, and allows you to write programs in a way which is closer to how humans think.
<br>

Internally the reason that Python code executes more slowly is because code is interpreted at runtime instead of being compiled to native code at compile time.<br>
### 2. Why is numpy so fast?:
At some time in the code let's take for example on a (500,500) matrix, the obtained time for numpy was 0.898 seconds whilst on  simple python lists it was 75.036, so it was basically 83 times faster, why?

<br>

Well, like i said, python is a high level language which limits it compared to other lower level languages, numpy which is mostly written in c( a low level language) makes it very fast and also, operations in Numpy are much faster because they take advantage of parallelism (which is the case of Single Instruction Multiple Data (SIMD)), while traditional for loop can't make use of it.
### 3. what if we use a python list and a matplotlib operation(np.dot())?:

Well, what happens is that the code runs at a fairly acceptable speed, somewhere between the 2. For example on a (500,500) array, the time elapsed is 8.583 seconds which makes it 8-9 times faster than a simple program with a list and a for loop.
So basically, why is it happenning?,<br>

well Numpy arrays are densely packed arrays of a homogeneous numerical data type.<br>
Python lists, by contrast, are arrays of pointers to objects, even when all of them are of the same type, memory is dynamically allocated , so when we pass 2 lists in a np.dot() method numpy will interpret it and convert it to an array,
<br> 

because we generated the matrices with the random module we also add the time taken+the time to process with the multiplication and we get this fairly acceptable time i got.<br>
### 4. What about numba?
<From Wikipedia, the free encyclopedia>:<br>
Numba is an open-source JIT compiler that translates a subset of Python and NumPy into fast machine code using LLVM, via the llvmlite Python package. It offers a range of options for parallelising Python code for CPUs and GPUs, often with only minor code changes. <br>

Well, in my case, i tried to boost up a bit the for loop and list method by using numba, this is the graph i obtained:<br>
![With numba](/img/numba.png "numba") <br>
<br>

This Graph showcase just how much numba made the program run so much faster, last time the speed on a (500,500) matrix was about 75.036, after boosting the program with numba the speed was an incredible....19.97896638999373 seconds, it seems little but this is a great achievement given  the time it took initially to run it, i mean compare these 2 graphs:
<br>                                       
                                             
![Original one](/img/task.png "first image") ![With numba](/img/numba.png "numba")<br>
<br>

Using numba.jit the speed increased by almost 4, this is amazing when seen on a bigger picture, imagine if we had to work with a (10000,10000) matrix, the increase in speed would be more significant.

<br><br><br>
Made with 😍, a lot of research, trial and debugging by `Shadowblade` for `GCI 2019`, Opensource 
